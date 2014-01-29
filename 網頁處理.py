from html.parser import HTMLParser
import os

class 賽馬會網頁剖析工具(HTMLParser):
	剖析結果 = []
	字體內量 = 0
	表格內 = 0
	def 剖析網頁檔案(self, 檔名):
		檔案 = open(檔名)
		資料 = 檔案.read()
		檔案.close()
		return self.剖析網頁(資料)
	def 剖析網頁(self, 資料):
		self.初始化剖析結果()
		self.feed(資料)
		return self.目前剖析結果()
	def 初始化剖析結果(self):
		self.剖析結果 = []
		self.表格內 = 0
		self.開始 = False
	def 目前剖析結果(self):
		return self.剖析結果
	def handle_starttag(self, tag, attrs):
		屬性表 = dict(attrs)
		if tag == 'table' and 'id' in 屬性表 and \
			'markSixResultTable' in 屬性表['id']:
			self.開始 = True
			self.剖析結果.append('')
		if self.開始:
			if tag == 'table':
				self.表格內+=1
			if tag=='td':
				self.剖析結果.append('')
			elif tag=='img' and '_' in 屬性表['src']:
#				print(屬性表['src'])
#				print(屬性表['src'].split('_')[1])
				self.剖析結果[-1] += 屬性表['src'].split('_')[1]
#			print(tag)
	def handle_endtag(self, tag):
		if self.開始:
			if tag == "table":
				self.表格內-=1
				if self.表格內==0:
					self.開始 = False
	def handle_data(self, data):
		if self.開始:
			self.剖析結果[-1] += data.strip()
#			print('', data.strip(),'',end='',sep='')

if __name__ == "__main__":
	檔案所在='/home/ihc/桌面/六合彩/'
	網頁剖析工具 = 賽馬會網頁剖析工具(strict=False)
	資料=[]
	for 檔名 in os.listdir(檔案所在):
		if 檔名.endswith('.html'):
			a = 網頁剖析工具.剖析網頁檔案('{0}/{1}'.format(檔案所在,檔名))
#			print(a[7:])
			資料.extend(a[7:])
			資料.append('')
#'12/035', '27/03/2012', '', '', '02', '07', '17', '25', '30', '43', 'special', '38', '',
#	print(資料[:])
	for 所在 in range(0,len(資料),13):
		一筆=資料[所在+4:所在+10]+[資料[所在+11],資料[所在+1]]
		for 號碼 in 一筆:
			print(號碼,end=' ')
		print()
