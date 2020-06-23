# -*- coding: utf-8 -*-
def batting_points(d):
    """This function is used for calculating batting points.
    It takes a dictionary as input.
    Dictionary must have the following fields:
        'scored'-indicating runs scored
        'faced'-number of balls faced by the player
        'fours'-Number of boundaries(4s) hit by the player
        'sixes'-Number of Sixes(6s) hit by the player    
    """
    if d['faced']!=0:
        pts=d['scored']//2
        if d['scored']>=50:
            pts+=5
        if d['scored']>=100:
            pts+=10
        strk=d['scored']/d['faced']*100
        if strk>=80 and strk<=100:
            pts+=2
        if strk>100:
            pts+=4
        pts=pts+d['fours']+d['sixes']*2
        return pts
    return 0
        
def bowling_points(d):
    """This function is used for calculating bowling and fielding points.
    It takes a dictionary as input.
    Dictionary must have the following fields:
        'bowled'-number of balls bowled by the player
        'wkts'-number of wickets
        'given'-number of runs given
        'catches'-number of catches taken
        'stumping'-number of stumpings done
        'run_out'-number of run outs
    """
    if d['bowled']!=0:
        pts=d['wkts']*10
        if d['wkts']>=3:
            pts+=5
        if d['wkts']>=5:
            pts+=10
        overs=d['bowled']/6
        ecr=d['given']/overs
        if ecr>=3.5 and ecr<=4.5:
            pts+=4
        elif ecr>=2 and ecr<3.5:
            pts+=7
        elif ecr<2:
            pts+=10
        pts=pts+(d['catches']+d['stumping']+d['run_out'])*10
        return pts
    return 0

if __name__=='__main__':
    p3={'bowled':60,'wkts':3,'given':34,'catches':0,'stumping':0,'run_out':0}
    print(bowling_points(p3))