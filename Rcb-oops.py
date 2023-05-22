class Rcb:
    def __init__(self,result):
        self.result=result

    def lost(self):
        print('Will see in the next Season')    


    def won(self):
        print('Ee sala cup Namade')     


def team():
    result=input('whether the team performed well? type (yes or no):' )
    if result =='yes':
         myobj=Rcb(result)
         myobj.won()
    elif result == 'no':
        myobj1=Rcb(result)
        myobj1.lost()
    else:
        print('Invalid result')
        team()
team()