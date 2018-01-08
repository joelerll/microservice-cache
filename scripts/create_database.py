import pymysql.cursors
import os
import codecs
import csv
from random import randint

user = ''
password = ''
db = ''
host = ''
with open('.env', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		user = row['user']
		password = row['password']
		db = row['db']
		host = row['host']

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

folders = ['business', 'entertainment', 'politics', 'sport', 'tech']
dir_path = os.path.dirname(os.path.realpath(__file__))

for folder_name in folders:
	path = dir_path + "/../dataset/" + folder_name
	files_names = os.listdir(path)
	for file_name in files_names:
		file_object = codecs.open(path + "/" + file_name, "r",encoding='utf-8', errors='ignore')
		contenido_file = file_object.read()
		parrafos = contenido_file.split('\n')
		parrafos = [parrafo for parrafo in parrafos if parrafo != '']  # eliminar los espacios con coma
		titulo = parrafos[0].strip()
		subtitulo = parrafos[1].strip()
		articulo = '\n'.join(parrafos[2:]).strip()
		file_object.close()
		try:
		    with connection.cursor() as cursor:
		        sql = "INSERT INTO `noticias` (`titulo`, `subtitulo`, `articulo`, `contador`) VALUES (%s, %s, %s, %s)"
		        cursor.execute(sql, (titulo, subtitulo, articulo, randint(0, 50)))
		    connection.commit()
		    file_object.close()
		except:
			print('Un error en insertar')
			pass
connection.close()
		