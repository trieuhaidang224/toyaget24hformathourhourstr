# region import bailam_f
from s00_bailam import get_24hformat_hour as bailam_f
# endregion import bailam_f


# region chambai
from s02_chambai import chambai

# region testkey_list
testcase_list = [
  {'input': {'hour_str': '6am'}, 'output': '6', 'tc_name': 'tc00'},

  {'input': ['6am'], 'output': '6', 'tc_name': 'tc01'},
  {'input': ['7 am'], 'output': '7', 'tc_name': 'tc02'},
  {'input': ['8AM'], 'output': '8', 'tc_name': 'tc03'},
  {'input': ['9 AM'], 'output': '9', 'tc_name': 'tc04'},

  {'input': ['6pm'], 'output': '18', 'tc_name': 'tc05'},
  {'input': ['7 pm'], 'output': '19', 'tc_name': 'tc06'},
  {'input': ['8PM'], 'output': '20', 'tc_name': 'tc07'},
  {'input': ['9 PM'], 'output': '21', 'tc_name': 'tc08'},

  {'input': ['10 AM'], 'output': '10', 'tc_name': 'tc09'},
  {'input': ['11 AM'], 'output': '11', 'tc_name': 'tc10'},
  {'input': ['10 PM'], 'output': '22', 'tc_name': 'tc11'},
  {'input': ['11 PM'], 'output': '23', 'tc_name': 'tc12'},

  {'input': ['07:15AM'], 'output': '7', 'tc_name': 'tc13'},
  {'input': ['02:49PM'], 'output': '14', 'tc_name': 'tc14'},
  {'input': ['06:46 AM'], 'output': '6', 'tc_name': 'tc15'},
  {'input': ['00:54'], 'output': '0', 'tc_name': 'tc16'},
  {'input': ['0606PM'], 'output': '18', 'tc_name': 'tc17'},
  {'input': ['08:24 AM'], 'output': '8', 'tc_name': 'tc18'},
  {'input': ['1006 AM'], 'output': '10', 'tc_name': 'tc19'},
  {'input': ['0252 PM'], 'output': '14', 'tc_name': 'tc20'},
  {'input': ['09:24AM'], 'output': '9', 'tc_name': 'tc21'},
  {'input': ['0802 AM'], 'output': '8', 'tc_name': 'tc22'},
  {'input': ['05:41 PM'], 'output': '17', 'tc_name': 'tc23'},
  {'input': ['0309'], 'output': '3', 'tc_name': 'tc24'},
  {'input': ['03:58 PM'], 'output': '15', 'tc_name': 'tc25'},
  {'input': ['10:16'], 'output': '10', 'tc_name': 'tc26'},
  {'input': ['23:38'], 'output': '23', 'tc_name': 'tc27'},
  {'input': ['08:21'], 'output': '8', 'tc_name': 'tc28'},
  {'input': ['0848'], 'output': '8', 'tc_name': 'tc29'},
  {'input': ['07:47 PM'], 'output': '19', 'tc_name': 'tc30'},
  {'input': ['09:39 PM'], 'output': '21', 'tc_name': 'tc31'},
  {'input': ['0945'], 'output': '9', 'tc_name': 'tc32'},
  {'input': ['01:45PM'], 'output': '13', 'tc_name': 'tc33'},
  {'input': ['07:44PM'], 'output': '19', 'tc_name': 'tc34'},
]
# endregion testkey_list

ketqua_list = []
for tc in testcase_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_BAILAM = chambai(tc, bailam_f)

  ketqua_list.append({
    'tc_name': tc['tc_name'],
    'tc_score': tc_score,
    'o_TESTCASE': tc['output'],
    'o_BAILAM': o_BAILAM,
  })
# endregion chambai

# region in ketqua
print('---ketqua chitiet')
for kq in ketqua_list:
  print(f'''
{kq['tc_name']} {kq['tc_score']}
o_TESTCASE = {kq['o_TESTCASE']}
o_BAILAM   = {kq['o_BAILAM']}
  '''.strip() + '\n')

print('\n---ketqua')
for kq in ketqua_list:
  print(f'''{kq['tc_name']} {kq['tc_score']}''')
# endregion in ketqua
