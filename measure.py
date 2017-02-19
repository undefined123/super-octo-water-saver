import sqlite3

class tank:
	def __init__(self):
		self.conn=sqlite3.connect('super_water')
		self.ctrl=self.conn.cursor()
		self.table="DIMENSIONS"
		self.head_water="MAXWATER"
		self.head_height="HEIGHT"
		self.head_diameter="DIAMETER"
		self.ctrl.execute("create table if not exists {tn}({m} int not null,{h} real not null,{d} real not null)"\
		.format(tn=self.table,m=self.head_water,h=self.head_height,d=self.head_diameter))
	def insert_d(self):
		try:
                        self.max_water=int(raw_input("Enter the maximum water"))
                        self.height=float(raw_input("Enter the maximum height of the water tank"))
                        self.diameter=float(raw_input("Enter the base diameter of the water tank"))
                except ValueError:
                        print "Enter a floating point value"
                        raise
		self.ctrl.execute("insert into {tn} values({m},{h},{d})"\
		.format(tn=self.table,m=self.max_water,h=self.height,d=self.diameter))
		self.conn.commit()
	def select_max(self):
		self.ctrl.execute("select * from DIMENSIONS order by rowid desc limit 1")
		for self.row in self.ctrl:
			self.max_water=self.row[0]
			self.height=self.row[1]
			self.diameter=self.row[2]
	def __del__(self):
		self.conn.close()
if __name__ == "__main__":
	s=tank()
	s.insert_d()	
	s.select_max()
	print s.max_water,s.height,s.diameter
