#encoding:utf-8
#!/usr/bin/env python
import os,sys,re
import time

class Washermachine:
	count=0
	Address="..."
	produce_data="..."
	def __init__(self,voltage=220,rank=1,water=100,scour=5):
		self.voltage=voltage
		self.rank=rank
		self.__water=water
		self.scour=scour
		Washermachine.count +=1
	def add_water(self,water,scour):
		self.__water=water
		self.scour=scour
	@property #装饰器property为只读装饰器，必须在setter装饰器前面，修改变量的装饰器为setter。
        def water(self):
                return self.__water
	
	@water.setter  #@water<var>.setter 装饰器将函数装饰为属性，使用等号赋值，不能用调用函数的方式,
	def water(self,water): #必须是私有变量名去掉__的名称加.setter
		if 0<water<500:
			self.__water=water
		else:
			print("Set water level wrong...")
	
	def set_start(self):
		print("Add water: "+str(self.__water))
		print("Add scour: "+str(self.scour))
		print("Start washing...")
	@classmethod #类方法的定义和使用,必须有cls
	def set_factory_config(cls,count=0,Address1="XIningdianqi",produce_data1="2019-8-20"):
		print("Using count number: "+str(count))
		Washermachine.Address=Address1
		Washermachine.produce_data=produce_data1



if __name__=="__main__":
	start_time=time.time()
	obj1=Washermachine(215,2)
	print("Begin configure:{}\t{}".format(obj1.Address,obj1.produce_data))
	#print("Initialization parameter: {0}\t{1}".format(str(obj1.water),str(obj1.scour))
	obj1.water=400  #经过装饰的函数只能用=号赋值
	print("Initialization water: "+str(obj1.water))
	print("Initialization scour: "+str(obj1.scour))
	print("Voltage Setting: "+str(obj1.voltage))
	print("Ranking Setting: "+str(obj1.rank))
	obj1.add_water(100,50)
	print("Start numbers: "+str(Washermachine.count))
	obj1.set_start()

	obj2=Washermachine(225,2)
	print("Start numbers: "+str(Washermachine.count))
	####recovery out factory configure
	obj2.set_factory_config()
	print("out factory configure:{0}\t{1}".format(obj2.Address,obj2.produce_data))
	end_time=time.time()
	print("Elapse time: "+str(end_time-start_time))
