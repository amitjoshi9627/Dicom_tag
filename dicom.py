import pydicom as dicom

def write_to_file(ds,name):
	with open(name,'w') as dcm:
		count_tag = 0
		for tag in ds.keys():
			dcm.write('{}: {}\n'.format(count_tag,tag))
			count_tag+=1
			
def display_tag(ds):
	count_tag = 0
	for tag in ds.keys():
		print("{}: {}".format(count_tag,tag))
		count_tag+=1


data_1 = dicom.dcmread("bmode.dcm")
dict_data_1 = dict(data_1)
display_tag(dict_data_1)
write_to_file(dict_data_1,"File1.txt")


data_2 = dicom.dcmread("ttfm.dcm")
dict_data_2 = dict(data_2)
display_tag(dict_data_1)
write_to_file(dict_data_2,"File2.txt")


