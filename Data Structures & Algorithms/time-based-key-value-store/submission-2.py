# timeMap = { 'key1': [ (val1,T1) , (val2,T2) ] , 'key2': [ (val1,T1) , (val2,T2) ] }
class TimeMap:

    def __init__(self):
        self.timemap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in  self.timemap:
            self.timemap[key].append((value,timestamp))
        else:
            self.timemap[key]=[(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        result= ""
        if key in self.timemap:
            left,right=0,len(self.timemap[key])-1
            while left<=right:
                m=(left+right)//2
                if self.timemap[key][m][1]<=timestamp :
                    result = self.timemap[key][m][0]
                    left=m+1
                else:
                    right=m-1
        return  result









