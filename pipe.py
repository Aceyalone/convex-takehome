import abnb_data as abnb

def build():
	base_data = abnb.get_list_summary()
	base_data = base_data.merge(abnb.get_list_details(), how='left', on='id')
