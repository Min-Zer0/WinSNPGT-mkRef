import os
import sys
import time
import datetime

Section_len_half = 200

def Getwd():
	for line in open('../install_dir'):
		chr_dir = line
	dir_list = chr_dir[1:].split("\\")[:-1]
	Path = "/cygdrive/" + dir_list[0][:-1] + "/"
	for i in range(len(dir_list)-1):
		Path = Path+'"'+dir_list[i+1]+'"'+"/"
	return Path

def ReadConfig():
	with open('../Reference_Genome/GenomeAnalysis.config.txt', 'r') as f:
		Config_info = f.readlines()
		spec_exit_list=[]
		for info in Config_info:
			if ">>" in info:
				spec = info[2:].replace(" ", "").replace("\t", "",).replace("\n", "",)
				spec_exit_list.append(spec)
	
	spec = input("\n\tspecies name: ").strip().replace(" ","")
	snpnum = input("\tSNP num: ").strip().replace(" ","")
	LineType = input("\t(Inbred/Hybrid) Line: ").strip().replace(" ","")
	if spec == "":
		spec = "Spec"
	if snpnum =="":
		snpnum = "000"
	if LineType =="":
		LineType = "Line"
	line_type = snpnum+"_"+LineType
	if spec in spec_exit_list:
		formatted_datetime = str(datetime.datetime.now().strftime("%H%M%S"))
		user_in = input('''  
[ %s ] is a duplicate of the species name in the online database! 
	It is recommended to change the species name.
	Type the new species name below and enter.
	By default, the system will change the name to [ %s ] by typing enter.
: '''%(spec,spec+formatted_datetime))
		if user_in == "":
			spec = spec+formatted_datetime
		else:
			spec = user_in.strip().replace(" ","")
	with open('../Reference_Genome/GenomeAnalysis.config.txt', 'a') as f_w:
		f_w.write('\n\n>> %s\n> %s []'%(spec,line_type))
		f_w.write('''
** ID=%s(https://iagr.genomics.cn/CropGS/#/PopulationBrowse?gstp_id=%s)
** Species=%s
** Sample type=unknown
** Sample number=unknown
** SNP number=unknown
** Traits number=unknown
** Paper=unknown | [unknown] (https://iagr.genomics.cn/CropGS/#/)
'''%(formatted_datetime,formatted_datetime,spec))
	return spec,line_type

def SplitRef(Ref_file, Chr_list):
    os.system("mkdir ./Chr_fa")
    for ChrNum in Chr_list:
        os.system("/tools/samtools-1.16.1/samtools.exe faidx %s %s > ./Chr_fa/%s.fasta" % (Ref_file, ChrNum, ChrNum))
        os.system("awk '{print $1,$2}' %s.fai > ./lengths.txt" % (Ref_file))

def Find_SNP_Section(Chr_intervals, Section_len_half, Chr_len):
    SNP_section = []
    for SNP_pos in Chr_intervals:
        if SNP_pos < Section_len_half:
            section = [0, SNP_pos + Section_len_half]
            SNP_section.append(section)
        elif SNP_pos + Section_len_half > Chr_len:
            section = [SNP_pos - Section_len_half, Chr_len]
            SNP_section.append(section)
        else:
            section = [SNP_pos - Section_len_half, SNP_pos + Section_len_half]
            SNP_section.append(section)
    return SNP_section

def merge_ranges(ranges):
    sorted_ranges = sorted(ranges)
    merged_ranges = []
    for start, end in sorted_ranges:
        if merged_ranges and start <= merged_ranges[-1][1]:
            merged_ranges[-1] = (merged_ranges[-1][0], max(end, merged_ranges[-1][1]))
        else:
            merged_ranges.append((start, end))
    return merged_ranges

def Movefile():
	spec_line =  ReadConfig()
	print(spec_line)
	os.system('mv -f %sMake_RefGenome/* ./  '%(Getwd()))
	ori_document = ["picard.jar","mkRef.py","README.txt"]
	now_document = []
	for fasta_bim in os.listdir("./"):
		now_document.append(fasta_bim)
	if len(list(set(now_document)-set(ori_document))) ==2:
		os.system('gunzip ./* >/dev/null 2>&1 &')
		Ref = ""
		for file_name in os.listdir("./"):
			if ".fa" in file_name or ".fasta" in file_name:
				Ref = file_name
		os.system("cp ./%s %s.fasta" %(Ref, spec_line[0]))
		os.system("mv ./%s %sMake_RefGenome/" %(Ref, Getwd()))
		return spec_line
	else:
		error_document = list(set(now_document)-set(ori_document))
		document_str = ' '.join([str(elem) for elem in error_document])
		os.system("mv %s  %sMake_RefGenome/" %(document_str,Getwd()))
		print("\n"+70*"-"+"\nInput file Error !\nPlease check files *.fasta/*.gz and *.bim in Make_RefGenome/")
		sys.exit()
		
def MakeREF(spec_line):
	os.system("awk '{position=$1\":\"$4\"-\"$4;print position}' \
			./*.bim > %s.intervals" %(spec_line[1]))

	Ref_file = spec_line[0]+".fasta"
	intervals_file = "%s.intervals" %(spec_line[1])

	os.system("/tools/samtools-1.16.1/samtools.exe faidx %s" % (Ref_file))
	os.system("java -jar picard.jar CreateSequenceDictionary -R %s" % (Ref_file))

	Chr_list = []
	intervals_df = open(intervals_file, 'r')
	for line in intervals_df:
		ChrNum = line[:-1].split(":")[0]
		if ChrNum not in Chr_list:
			Chr_list.append(ChrNum)
	intervals_df.close()

	SplitRef(Ref_file, Chr_list)

	fw = open("./SNP_intervals.bed",'w')
	for ChrNum in Chr_list:
		Chr_len = ''
		for line in open("./lengths.txt", "r"):
			if line.split(" ")[0] == ChrNum:
				Chr_len = int(line[:-1].split(" ")[1])
		Chr_intervals = []
		for line in open(intervals_file, 'r'):
			if line[:-1].split(":")[0] == ChrNum:
				Chr_intervals.append(int(line[:-1].split(":")[1].split("-")[0]))
		SNP_section = Find_SNP_Section(Chr_intervals, Section_len_half, Chr_len)
		SNP_meraged_section =  merge_ranges(SNP_section)
		for SNP_section in SNP_meraged_section:
			fw.write(str(ChrNum)+"\t")
			fw.write(str(SNP_section[0])+"\t")
			fw.write(str(SNP_section[1])+"\n")
	fw.close()

	os.system("/tools/seqtk-1.3/seqtk.exe subseq %s SNP_intervals.bed > SNP_intervals.fasta"%(Ref_file))
	os.system("rm -rf lengths.txt SNP_intervals.bed Chr_fa/ ")

	result_file = spec_line[0]+"_"+spec_line[1]
	os.system("mkdir %s" %(result_file))
	os.system("mv %s.fasta %s.fasta.fai %s.dict %s.intervals SNP_intervals.fasta %s" 
		%(spec_line[0],spec_line[0],spec_line[0],spec_line[1],result_file))

	os.system("/tools/bowtie2-2.4.5-mingw-x86_64/bowtie2-build %s/%s.fasta %s/%s"
		%(result_file,spec_line[0],result_file,spec_line[0]))
	os.system("/tools/bowtie2-2.4.5-mingw-x86_64/bowtie2-build %s/SNP_intervals.fasta %s/SNP_intervals"
		%(result_file,result_file))
	os.system("rm -rf ../Reference_Genome/%s"%(result_file))
	os.system("mv %s ../Reference_Genome/"%(result_file))

def Processing(num,start):
	i = 80
	a = "*" * num
	b = "." * (i - num)
	c = (num / i) * 100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")


os.system('cat ./README.txt')
start = time.perf_counter()
spec_line = Movefile()
print(42*"-","Runing",43*"-")		
Processing(20,start)
MakeREF(spec_line)
Processing(60,start)
Processing(80,start)
os.system("mv ./*.bim %sMake_RefGenome/" %(Getwd()))
print("\n"+40*"-"+"Completed !!!"+40*"-"+"\n"+"Please close this window.")