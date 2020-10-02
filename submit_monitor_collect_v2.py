import json
import os

QUEUES =  {'1':'cdm8_b_g_sc_default','2':'cdm8_f_g_bc_default',
           '3':'cdm8_h_g_gc_default','4':'mms7306_b_g_gc_default'}
submit_jobs = True
run_commands = False
STATUS_FILE = 'status_file.json'
status = json.loads(open(STATUS_FILE).read())
WORK_DIR = './work'

jobs = ['449_C','449_R','453_P','453_F','455_D','455_M','456_D','456_L','475_W','475_S']

MAIN_DIR = os.getcwd()

def get_job_args():
    wall_time = int(input("Enter wall time in hrs:"))
    memory = int(input("Enter memory in gb:"))
    print('QUEUE')
    print('1. cdm8_b_g_sc_default\n')
    print('2. cdm8_f_g_bc_default\n')   
    print('3. cdm8_h_g_gc_default\n')   
    print('4. mms7306_b_g_gc_default\n')
    queue = QUEUES[str(input("Choose queue from above:")).strip()]

    return wall_time, memory, queue

def change_job_content(old_job_lines,wall_time,memory,queue):
    template = "#PBS -l nodes=1:ppn=1\n#PBS -l walltime={0}:00:00\n#PBS -l pmem={1}gb\n#PBS -l mem={1}gb\n#PBS -A {2}\n#PBS -j oe\n"
    new_job_content = template.format(wall_time,memory,queue)
    
    for line in old_job_lines:
        if not line.startswith('#PBS'):
            #print(line)
            new_job_content+=line
    
    print(new_job_content)
    return new_job_content
    
wall_time = None
memory = None
queue = None

for job in jobs:
    os.chdir(WORK_DIR+'/'+job)
    print(os.getcwd())
    files = os.listdir('.')
    if submit_jobs:
        # There should be a main .job file and a bunch of other job files
        for file in files:
            if file.endswith('.job'):
                print(file)
                f = open(file)
                old_job_lines = f.readlines()
                f.close()
                if wall_time==None:
                    wall_time, memory, queue = get_job_args()
                else:
                    pass
                new_job_content = change_job_content(old_job_lines,wall_time,memory,queue)
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
