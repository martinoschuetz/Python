import swat

conn = swat.CAS("centis.example.local", 5570, authinfo="~/_authinfo", caslib="casuser")
conn.serverstatus()
#conn.close()