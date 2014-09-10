from ipython_doctester import test
import pickle
function_names = ['hello','cube','too_long_for_twitter','greatest','calculate','menu_specials','return_first_item',
                  'add_exclamation','find_student','count_fs','starts_or_ends_with_z','sum_of_all_strings','squares_list',
                  'remove_vowels','remove_words_with_vowels']
bonus_function_names = ['multiply_string','make_HTML','hello_many','stretch_string','spelling_bee']

#in case they've messed with the docstrings we read them in from a pickled list of the correct doc strings
with open('ex_1_doc_strs.pkl') as doc_f:
    fn_doc_strings = pickle.load(doc_f)
with open('ex_1_bonus_doc_strs.pkl') as doc_f:
    bonus_fn_doc_strings = pickle.load(doc_f)

for fn,doc_str in zip(function_names,fn_doc_strings):
    globals()[fn].__doc__ = doc_str
    
for fn,doc_str in zip(bonus_function_names,bonus_fn_doc_strings):
    globals()[fn].__doc__ = doc_str


failed_functions, failed_bonus_functions = [], []
passed, failed = 0,0

for f_nm in function_names:
    print(f_nm)
    f = globals()[f_nm]
    if not test(f).failed:
        passed+=1
    else:
        failed_functions.append(f_nm)
        failed+=1

passed_bonus, failed_bonus = 0,0
for f_nm in bonus_function_names:
    print(f_nm)
    f = globals()[f_nm]
    if not test(f).failed:
        passed_bonus+=1
    else:
        failed_bonus_functions.append(f_nm)
        failed_bonus+=1

print('Failed_functions: {}'.format(failed_functions))
print('Failed_bonus_functions: {}'.format(failed_bonus_functions))
print('Passed {}, Failed {}, Passed_bonus {}, Failed_bonus {}'.format(passed,failed,passed_bonus,failed_bonus))
