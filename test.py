from models.settings import Settings
import helpers.services as serv
import helpers.firebase as fb

# settings = Settings()
# # serv.load_settings(settings)

# # fb.write_settings(settings)

# set_dict = fb.read_data('settings', 'signal')
# settings.from_dict(set_dict)
# # print(set_dict)
# print('-------------------------------------------')
# print(settings.__dict__)
fb.chande_signal_trigger()