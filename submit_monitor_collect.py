import json
import os

QUEUES =  {'1':'cdm8_b_g_sc_default','2':'cdm8_f_g_bc_default',
           '3':'cdm8_h_g_gc_default','4':'mms7306_b_g_gc_default'}
submit_jobs = False
run_commands = True
STATUS_FILE = 'status_file.json'
status = json.loads(open(STATUS_FILE))

jobs = ['417_D','417_P','439_E','439_K','446_C','446_K']

MAIN_DIR = os.getcwd()

def change_job_args():
    template = ''''

#PBS -l nodes=1:ppn=1

#PBS -l walltime={0}:00:00

#PBS -l pmem={1}gb

#PBS -l mem={1}gb

#PBS -A {2}
#PBS -j oe

    '''
    wall_time = int(input("Enter wall time in hrs:"))
    memory = int(input("Enter memory in gb:"))
    print('QUEUE')
    print('1. cdm8_b_g_sc_default\n')
    print('2. cdm8_f_g_bc_default\n')   
    print('3. cdm8_h_g_gc_default\n')   
    print('4. mms7306_b_g_gc_default\n')
    queue = QUEUES[str(input("Choose queue from above:")).strip()]
    
    new_job_content = template.format(wall_time,memory,queue)
    
    for line in old_job_lines:
        if not line.startswith('#PBS'):
            new_job_content+='\n'+line+'\n'
    
    return new_job_content
    
for job in jobs:
    os.system('chdir '+job)
    files = os.listdir('.')
    if submit_jobs:
        # There should be a main .job file and a bunch of other job files
        for file in files:
            if file.endswith('.job'):
                f = open(file)
                old_job_lines = f.readlines()
                f.close()
                new_job_content = change_job_args(old_job_lines)
                f = open(file,'w')
                f.write(new_job_content)
                f.close()
        
        try:
            f = open(job+'.job')
            os.system('qsub '+job+'.job')   
            try:
                status[job] = 'Running'
            except KeyError:
                print(job,' not found in status dictionary.. Something might be wrong!')
            
        except IOError:
            print('Main job file not found for ',job)
            print('Doing nothing..')
            continue
        
    elif run_commands:
        # There should be a main .sh file
        try:
            f = open(job+'.sh')
            for line in f:
                os.system(line.strip())
            
            try:
                status[job] = 'Running'
            except KeyError:
                print(job,' not found in status dictionary.. Something might be wrong!')
            
        except IOError:
            print('Main sh file not found for ',job)
            print('Doing nothing..')
            continue

    os.chdir(MAIN_DIR)
    break