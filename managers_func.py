import subprocess
from telegram import Bot
from decouple import config
import time
import helpers.tlg as tel
import os

old_timestamp = 0

api_token = None

def start_program(i: int):
    command = f"nohup python3 main_1.py {i} > output{i}.log 2>&1 &"
    # subprocess.Popen(command, shell=True)
    subprocess.Popen(['python3', 'main_1.py', str(i)], stdout=open(f'output{i}.log', 'w'), stderr=subprocess.STDOUT)

def write_pids_to_file(pids, filename):
    with open(filename, 'w') as file:
        for pid in pids:
            file.write(str(pid) + '\n')

def read_pids_from_file(filename):
    with open(filename, 'r') as file:
        pids = [int(pid.strip()) for pid in file.readlines()]
    return pids

async def kill_processes(pids):
    for pid in pids:
        try:
            os.kill(pid, 9)  # Sends a SIGKILL signal to the process
            msg = f"Process with PID {pid} killed successfully"
            await tel.send_inform_message(msg, '', False)
            print(msg)
        except OSError:
            print(f"Failed to kill process with PID {pid}")

def run_signals():
    num_processes = 4
    process_pids = []

    # Запускаем многопроцессовую программу
    for i in range(num_processes):
        start_program(i)
        print('sleep 15')
        time.sleep(15)

    # Подождем несколько секунд, чтобы процессы успели стартовать
    print('sleep 15')
    time.sleep(15)

    # Находим PID процессов с именем 'main.py'
    for pid in os.listdir('/proc'):
        try:
            pid = int(pid)
            cmdline = open(os.path.join('/proc', str(pid), 'cmdline'), 'rb').read().decode('utf-8')
            if 'python3' in cmdline and 'main_1.py' in cmdline:
                process_pids.append(pid)
        except (ValueError, FileNotFoundError, IOError):
            continue

    # Записываем PID в файл
    write_pids_to_file(process_pids, 'process_pids.txt')

    print(f"Запущено {len(process_pids)} процессов с PID: {process_pids}")

async def check_process_pids():
    if not os.path.exists('process_pids.txt'):
        return
    # Read the PIDs from file
    with open('process_pids.txt', 'r') as file:
        pids = [int(pid.strip()) for pid in file.readlines()]

    for pid in pids:
        try:
            os.kill(pid, 0)  # Check if process exists
        except OSError:
            await kill_processes(read_pids_from_file('process_pids.txt'))
            os.remove('process_pids.txt')
            run_signals()


async def check_and_handle_message():
    global old_timestamp, api_token
    try:
        # Create a Telegram bot instance
        bot = Bot(token=api_token)

        # Get the latest message from the bot's chat
        updates = await bot.get_updates()
        message = ''
        if len(updates) > 0:
            message = updates[-1].message
        else: 
            return

        # Check if there is a new message
        if message is not None and old_timestamp != message.date.timestamp() and (time.time() - message.date.timestamp()) <= 30:
            old_timestamp = message.date.timestamp()
            if message.text == 'kill' or message.text == 'Kill':
                await kill_processes(read_pids_from_file('process_pids.txt'))
                os.remove('process_pids.txt')
            if message.text =='restart' or message.text == 'Restart':
                await kill_processes(read_pids_from_file('process_pids.txt'))
                os.remove('process_pids.txt')
                run_signals()
            if message.text =='start' or message.text == 'Start':
                run_signals()
            print("New message handled successfully!")
    except Exception as e:
        print("An error occurred:", str(e))