# Instagram-User-Scraper-2-JSON
安裝方法:<br>
cd /[PROJECT]<br>
python3.8 -m pip install -r request.txt --user<br>
<br>
執行:<br>
python3.8 run.py<br>
<br>
關於如何自動執行:<br>
sudo nano /etc/rc.local<br>
於最底一行加入<br>
sudo python3.8 /path/to/Instagram-User-Scraper-2-JSON/run.py &<br>
exit 0<br>
<br>
使用方法:<br>
	IG_user_List.txt - Instagram用戶名(一行一個)<br>
	ig_user_dumper - JSON格式輸出位置(以用戶名加上_log.json結尾)<br>
	注意更改自動更新時間:<br>
	schedule.every(1).hour.do(IG_SCRAP)<br>
	每一小時即行一次,可更改為<br>
	每分鐘<br>
	schedule.every(1).minutes.do(IG_SCRAP)<br>
	每日指定時間<br>
	schedule.every().day.at("00:00").do(IG_SCRAP) <br>
	指定星期+指定時間<br>
	schedule.every().tuesday.at("18:00").do(IG_SCRAP)<br>
<br>
本爬蟲用於在收集IG公開用戶之帳戶,以JSON格式輸出.<br>
為網頁資源在用而設,如下載JSON檔案後閣下可自行對JSON再進行從整網頁排版用途.
