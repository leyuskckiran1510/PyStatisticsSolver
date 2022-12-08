import requests
import json
import re
import os
import dotenv

dotenv.load_dotenv()


class Statistics:
    def __init__(self, data):
        self.raw_data = data
        self.data = data
        self.balanced_data = self.balance_continious_data()
        self._clean()
        self.N = sum([i[1] for i in self.data])
        self.x = [i[0] for i in self.data]
        self.f = [i[len(self.balanced_data[0])-1] for i in self.balanced_data] if len(self.balanced_data[0])!=1 else [i[1] for i in self.data]
        self.fx = [self.f[i]*self.x[i] for i in range(len(self.f))]
        self.midx = [(self.balanced_data[i][1]+self.balanced_data[i][0])/2   for i in range(len(self.f))] if len(self.balanced_data[0])==3  else [self.data[0] for i in range(len(self.f))]
        self.cumulative = self._cumulative()
        self.mean = self._mean()
        self.median = self._median()




    def _cumulative(self):
        cum_lis=[]
        for n,i in enumerate(self.data):
            cum_lis.append(i[1]+cum_lis[n-1] if n!= 0 else i[1])
        return cum_lis

        

    def balance_continious_data(self):
        if(len(self.data[0])!=3):
            print("in",self.data)
            return self.data
        offset = (self.data[1][0]-self.data[0][1])/2
        return [[i[0]-offset,i[1]+offset,i[2]] if i[0]!=0 else [i[0],i[1]+offset,i[2]] for i in self.data]     
        
        

    def _clean(self):
        temp=[]
        for i in self.data:
            if len(i)==3:
                temp.append([(i[0]+i[1])/2,i[2]])
            elif len(i)==2:
                temp.append([i[0],i[1]])
            elif len(i)==1:
                if i[0] not in temp:
                    temp.append([i[0],self.data.count([i[0]])])
                    
            else:
                temp.append([0,0])
        self.data = temp


    def _mean(self):
        return sum(list(map(lambda x:x[0]*x[1],self.data)))/self.N

    def stat_print(self):
        if len(self.balanced_data[0])==3:
            print("raw_X\t\tX\t\tmid-x\tf\tcf\tfx")
        elif len(self.balanced_data[0])==2:
            print("Weights:-\tFrequency:-\t")
        for i in range(len(self.data)):
            print(f"{self.raw_data[i][:-1]}\t{self.balanced_data[i][:-1]}\t{self.midx[i]}\t{self.f[i]}\t{self.cumulative[i]}\t{self.fx[i]}")



    def _median(self):
        diff_dic={}
        for n,i in enumerate(self.cumulative):
                if i>self.N/2:
                    diff_dic[abs(i-(self.N/2))] = n
        a=sorted(diff_dic.items())[0][1]
        if len(self.balanced_data[0])==3:
            median_class = self.balanced_data[a]
            return median_class[0] +abs(median_class[0]-median_class[1]) * ((self.N/2 - self.cumulative[a-1])/self.f[a])
        elif len(self.balanced_data[0])==2:
            return self.data[a]
        return 0



def extract(name='a.jpg'):
    url = 'https://api.ocr.space/parse/image'
    with open(name, 'rb') as image_file:
        payload = {
            'apikey':os.getenv("API_KEY"),
            'language': 'eng',
            'isOverlayRequired': 'false',
            'FileType': '.Auto',
            'isTable': 'true',
            'scale': 'true',
            'OCREngine': '2',
            }
        response = requests.post(url,files={name:image_file},data=payload)
        try:
            return response.json()['ParsedResults'][0]['ParsedText']
        except KeyError as e:
            print("KeyError:- Avilable Keys are",response.json().keys())
        except Exception as e:
            print("Other Exceptio Occured ie:-",e)


def flatten_list(nested_list, flattened_list):
    for item in nested_list:
        if isinstance(item, list):
            flatten_list(item, flattened_list)
        else:
            flattened_list.extend([int(item)])


def parser(string):
    pattren=r"\d{1,9}[-|\s]\d{0,9}\s+\d+"
    final=[]
    string = string.replace("\t","    ").replace("\n","    ")
    matches = re.findall(pattren,string)
    for match in matches:
        blnk=[]
        lis = [i.split("-") for i in match.split(" ")]
        lis = [i for i in lis if i!=['']]
        flatten_list(lis,blnk) 
        final.extend([blnk])
    return final

def indvual(string):
    pattren = r"\d{1,9}"
    final=[]
    matches = re.findall(pattren,string)
    for match in matches:
        final.append([int(match)])
    return final
def test():
    vert='''3. Check the following requency distribUion talble, co1S
Weights (in kg) Number of stud
31 35   9
36 40   5
41-45   14
46-50   3
51-55   1
56 60   2
61 65   2
66 70   1
71 75   1
() What is class-interval for classes 31 35?
() How many students are there in the range of 41-45 kgs?
Salu

    '''
    hori='''Number of wickets
Number of bowlers
20-60
7
60-100
5
100-150
16
150-250
12
250-350
2
350-450
3
'''
    dis='''>140
4
>145
11
>150
29
>155
40
>160
46
>165
51
'''
    indv="25 36 42 55 60 62 73 75 78 95"

    #c= parser(extract('image3.png'))
    c= parser(hori)
    #c= indvual(indv)
    #print(c)
    d= Statistics(c)
    # pprint(d.raw_data)
    # pprint(d.data)
    # pprint(d.balanced_data)
    # pprint(d.cumulative)
    d.stat_print()
    print("Mean:-",d.mean)
    print("Median:-",d.median)
    
    
    



def main():
    test()
    pass



if __name__=="__main__":
    main()