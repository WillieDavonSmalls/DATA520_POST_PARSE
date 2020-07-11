#
# from bs4 import BeautifulSoup
# with open ('2.txt', 'r') as file:
#     thread = file.read().replace('\n','')
#
# thread = BeautifulSoup(thread, "html.parser")
#
# time_stamp = thread.select(".db_msg_metadata")
# subject = thread.select(".message-subject")
# author = thread.select(".author")
# post = thread.select(".vtbegenerated")
# print([time.text for time in time_stamp])
# print([subject_name.text.strip() for subject_name in subject])
# print([author_name.text.strip() for author_name in author])
# print([post_msg.text.strip() for post_msg in post])


for i in range(20):
    file_name = str(i) + ".txt"
    open(file_name, 'a').close()