from ipython_doctester import test
function_names = ['split_lines','join_lines','clean_line','chars_before_comma','print_file','square_list','write_squares',
                  'null_vector','checkboard','gen_poly','fit_poly','plot_data','word_extractor','read_squares',
                  'matrix_from_lists','multi_plot_data']

functions_for_manual_testing = []

passed, failed = 0,0
for f_nm in function_names[:-4]:
    f = globals()[f_nm]
    if not test(f).failed:
        passed+=1
    else:
        failed+=1

passed_bonus, failed_bonus = 0,0
for f_nm in function_names[-4:]:
    f = globals()[f_nm]
    if not test(f).failed:
        passed_bonus+=1
    else:
        failed_bonus+=1

