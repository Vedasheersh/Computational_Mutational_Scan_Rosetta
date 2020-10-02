import os

# SOME CONSTANTS (for now) 
##TODO##
# Make these as command-line variables later
NUM_TRAJ = 10 # number of trajectories for each mutant
SUPER_RESFILE = 'all.SuperResfile'
INTERFACE = True
PARTNERS = 'A_B'
METRICS = ['total_score','dG_binding']
TEMP_DIR = './temp'
INPUT_DIR = './inputs'
FLAGS_FILE = 'flags'
FLAGS_SCORE_FILE = 'flags_score'
XML_FILE = 'mutate_relax_minimize.xml'
JOB_FILE = 'job_template.sh'
WORK_DIR = './work'
RESULTS_DIR = './results'
INPUT_PDB = '6lzg_clean.pdb'
ROSETTA_DIR = '/gpfs/group/cdm8/default/rosetta/rosetta_bin_linux_2018.33.60351_bundle/main/source/bin'

WRITE_COMMANDS = True
# if True, make .sh files of just the commands (.job files are always written irrespective of this)

class Resfile(object):
    """docstring for Resfile"""
    def __init__(self, content,name):
        super(Resfile, self).__init__()
        self.content = content
        self.name = name
        self.filepath = TEMP_DIR+'/'+self.name+'.resfile'
        self.file = open(self.filepath,'w')
        self.file.write(self.content)
        self.file.close()    
        
    def __repr__(self):
        return self.filepath

class SuperResfile(object):
    """docstring for SuperResfile"""
    def __init__(self, filepath):
        super(SuperResfile, self).__init__()
        self.filepath = filepath
        try:
            self.file = open(self.filepath)
        except IOError:
            self.file = None

    def __next__(self):
        resfile = ''
        while True:
            try:
                line = next(self.file)
            except StopIteration:
                raise StopIteration
            # print(line)
            
            if 'RESFILE' in line:
                _, name = line.strip().split()
            
            elif line.strip()=='':
                continue
            
            elif 'STOP' in line:
                break

            else:
                resfile+=line

        return Resfile(resfile,name)
    
    def __iter__(self):
        return self
    
    def __len__(self):
        return

def main():
    JOBS = []
    # Make SuperResfile and make directories
    sfile = SuperResfile(INPUT_DIR+'/'+SUPER_RESFILE)
    MAIN_DIR = os.getcwd()
    for rf in sfile:
        CUR_DIR = WORK_DIR + '/' + rf.name
        os.chdir(os.path.abspath(CUR_DIR))
        
        os.system('mkdir '+CUR_DIR)
        os.system('cp {0} {1}/{2}.resfile'.format(str(rf),CUR_DIR,rf.name))
        os.system('cp {0}/{1} {2}/{1}'.format(INPUT_DIR,XML_FILE,CUR_DIR))
        os.system('cp {0}/{1} {2}/{1}'.format(INPUT_DIR,INPUT_PDB,CUR_DIR))
        f = open('{0}/{1}'.format(INPUT_DIR,FLAGS_FILE))
        flags = f.read()
        f.close()
        f = open('{0}/{1}'.format(INPUT_DIR,FLAGS_SCORE_FILE))
        flags_score = f.read()
        f.close()
        f = open('{0}/{1}'.format(CUR_DIR,FLAGS_FILE),'w')
        f.write(flags.format(INPUT_PDB,'1',rf.name+'.resfile'))
        f.close()
        f = open('{0}/{1}'.format(CUR_DIR,FLAGS_SCORE_FILE),'w')
        f.write(flags_score.format(PARTNERS))
        f.close()
        default_job_content = open(INPUT_DIR+'/'+JOB_FILE).read()
        main_job = CUR_DIR+'/'+'{0}.job'.format(rf.name)
        f = open(main_job,'w')
        f.write(default_job_content)
        
        if WRITE_COMMANDS:
            fcom = open('{0}.sh'.format(rf.name),'w')
            
        # Now write all the sub jobs
        for i in range(1,NUM_TRAJ+1):
            command = '{0}/rosetta_scripts.static.linuxgccrelease @flags -out:suffix _struct{1}\n'.format(ROSETTA_DIR,i)
            
            if WRITE_COMMANDS:
                fcom.write(command)
                
            sub_job = '{0}_struct{1}.job'.format(rf.name,i)
            ff = open(sub_job,'w')
            ff.write(default_job_content)
            ff.write(command)
            ff.close()
            f.write('qsub {0}\n'.format(sub_job))
            
        if WRITE_COMMANDS:
            fcom.write('{0}/InterfaceAnalyzer.static.linuxgccrelease -in:file:s *struct*.pdb @flags_score\n'.format(ROSETTA_DIR))
            fcom.close()
            
        f.close()
        JOBS.append(main_job)
        os.chdir(MAIN_DIR)
    
    return JOBS