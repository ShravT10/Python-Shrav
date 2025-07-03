#include<iostream>
using namespace std;

int main()
{
    int sleep;
    double ss;
    double bfs;   
    int bf;
    int lf;
    double lfs;
    int df;
    double dfs;
    char extra;
    int ep;
    int water;
    int ws;
    int sss;
    int sa;
    int ga;
    int gas;
    int ti;
    int tis;
    double ts;
    cout<<"*******THE VAISH SCORECARD*******\n";
    cout<<"Let's take our today's report !\n";
    cout<<"*********************************\n";
    cout<<"HOW MUCH HOURS OF SLEEP YOU HAD TODAY? :";
    cin>>sleep;
    if (sleep>8){
    
        cout<<"Well that is great that you had a 8+ hrs of sleep , but sleep more than 8 hrs make you sleepy and tired throughout the day.\n";
        cout<<"And yes there might be situtions like you didnt sleep enough yesterday or from many days , if so then its compeletely fine and great that you had this much sleep and rested good ! (hello hibernation qt)\n";}
    else{}
        
    
    switch(sleep){
        case 0:
        ss = 0;
        cout<<"HAWW vaish that is not good ! you should get a lot of rest and do very less work today !!\n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        break;
        case 1:
        ss = 1;
        cout<<"That is not good at all , please try getting more sleep today and dont drain yourself up\n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        break;
        case 2:
        ss = 1.5;
        cout<<"Why so poor performance vaish , please give yourself some rest and sleep , got get more sleep rn!\n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        break;
        case 3:
        ss = 2;
        cout<<"Well 3 hours sleep is not enough at all , whatever the reason maybe ! today you'll have rest whenever you can and no pushing yourself for any work\n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        break;
        case 4:
        ss = 2.5;
        cout<<"We can call is a lil less than enough sleep , but still you should get more sleep tomorrow and rest today as well \n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";;
        break;
        case 5:
        ss = 3;
        cout<<"Now thats some enough sleep , but still it is not good you can do better , you did now too tho !\n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        break;
        case 6:
        ss = 4;
        cout<<"Aye thats great now ! good you got a 6 hours sleep now you can be productive and active today , NICEU! \n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        break;
        case 7:
        ss = 5;
        cout<<"Babe well done !! now youll be energetic throughout the day and not be tired , you also made me real happy :D , aise hi aachi aachi nini krna roj roj ! MWAH \n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        cout<<"(CONGRATULATIONS YOU HAVE EARNED FULL SCORE , YAYYY i am proud of you !!!!)\n";
        break;
        case 8:
        ss = 5;
        cout<<"Babe well done !! now youll be energetic throughout the day and not be tired , you also made me real happy :D , aise hi aachi aachi nini krna roj roj ! MWAH \n";
        cout<<"*****POINTS YOU EARNED :  "<<ss<<"  *****\n";
        cout<<"(CONGRATULATIONS YOU HAVE EARNED FULL SCORE , YAYYY i am proud of you !!!!)\n";
        break;
        default:
        cout<<"please choose a valid response and make sure it's a integer (you can input approx value better than accurate values in decimals)\n";
        break;
        return 0;
    }
    cout<<"*****************NEXT********************\n";
    cout<<"HOW MUCH DID YOU ATE THROUGHOUT THE DAY ?\n";
    cout<<"*****************************************\n";
    cout<<"TELL ABOUT YOUR BREAKFAST\n";
    cout<<"(Choose an option)\n";
    cout<<"You ate?\n";
    cout<<"0. You ate nothing\n"<<"1. Just milk\n"<<"2. A mid breakfast like half chapati and bhaji\n"<<"3. Had a heavy breakfast (1 chapati , maggi , pasta etc) which made your tummy full\n";
    cout<<"Your choice:";
    cin>>bf;
    switch(bf){
        case 0:
        bfs=0;
        cout<<"Vaish aisa noko karo , youll become tired if no food . Very poor but it fine apan kuch khane jaate aaj hehe\n";
        cout<<"*****POINTS YOU EARNED :  "<<bfs<<"  *****\n";
        break;
        case 1:
        bfs=1.5;
        cout<<"Still not enaf, short break mein ya 10/11 baje kuch aur kha lena yaad se, and if drinking milk make sure you atleast have some biscuits or toasts\n";
        cout<<"*****POINTS YOU EARNED :  "<<bfs<<"  *****\n";
        break;
        case 2:
        bfs=3;
        cout<<"Thats very good work, try to make this kind of meal your everday one it would be very healthy , but yes dont push yourself , jitna kha sako utna khao :3\n"; 
        cout<<"*****POINTS YOU EARNED :  "<<bfs<<"  *****\n";
        break;
        case 3:
        bfs=5;
        cout<<"Wow vaish , that is a progress , well done . Aaj aap fhir energetic and active rahoge. Today is gonna be productive yayy !\n";
        cout<<"*****POINTS YOU EARNED :  "<<bfs<<"  *****\n";
        break;
        default:
        cout<<"choose a valid option, if your choice is not from the choice you can text me what you ate <3\n";
        break;
        return 0;
    }
    cout<<"*****************NEXT********************\n";
    cout<<"TELL ABOUT YOUR LUNCH\n";
    cout<<"(Choose an option)\n";
    cout<<"You ate?\n";
    cout<<"0. You ate nothing\n"<<"1. Ate a some food (like some snacks only, ya kuch halka sa sirf like fruit or something)\n"<<"2. Had good food (chapati bhaji , pasta etc)\n";
    cout<<"Your choice:";
    cin>>lf;
    switch(lf){
        case 0:
        lfs=0;
        cout<<"Vaish aisa karegi toh kaisa chalega re baby , text me in brief why you didnt eat we'll talk on it \n";
        cout<<"*****POINTS YOU EARNED :  "<<lfs<<"  *****\n";
        break;
        case 1:
        lfs=3.5;
        cout<<"Still not enaf, it is great that you ate , thoda aur kha sako toh bhi it fine , you'll just generate more energy and charge up ! but yes good you ate\n";
        cout<<"*****POINTS YOU EARNED :  "<<lfs<<"  *****\n";
        break;
        case 2:
        lfs=5;
        cout<<"Aye honey niceu !! you;re tummy must be full and you must be full of energy , you did greattttoo mwahh !\n"; 
        cout<<"*****POINTS YOU EARNED :  "<<lfs<<"  *****\n";
        break;
        default:
        cout<<"choose a valid option, if your choice is not from the choice you can text me what you ate <3\n";
        break;
        return 0;
    }
    cout<<"*****************NEXT********************\n";
    cout<<"TELL ABOUT YOUR DINNER\n";
    cout<<"(Choose an option)\n";
    cout<<"You ate?\n";
    cout<<"0. You ate nothing\n"<<"1. Ate some food (half chapati and bhaji , some fast food but less etc )\n"<<"2. Had good food (chapati bhaji with rice , Pet bharke junk food etc )\n"<<"3. Just drank milk\n";

    cout<<"Your choice:";
    cin>>df;
    switch(df){
        case 0:
        dfs=0;
        cout<<"It is sad you didnt eat anything , please go eat something still if there is time . And if there is valid reason then it is fine but talk it out with me \n";
        cout<<"*****POINTS YOU EARNED :  "<<dfs<<"  *****\n";
        break;
        case 1:
        dfs=3.5;
        cout<<"It is great that you ate something , thoda aur kuch extra kha sakte fruits vagera toh khao. If tummy mein jagha ho\n";
        cout<<"*****POINTS YOU EARNED :  "<<dfs<<"  *****\n";
        break;
        case 2:
        dfs=5;
        cout<<"Ayee thats perfectoo! me happy abhi tumko aachi nini aaigi and and youll be energetic kal. PS you earn yourself a kissie hehe (vo vese bhi mil hi jaati)\n"; 
        cout<<"*****POINTS YOU EARNED :  "<<dfs<<"  *****\n";
        break;
        case 3:
        dfs=1.5;
        cout<<"Honey , its still better than sleeping empty stomach , kuch khalo maan ho toh please. and agar koi reason ho and tummy full ho toh maat khao it fine , just tell me <3\n";
        cout<<"*****POINTS YOU EARNED :  "<<dfs<<"  *****\n";
        default:
        cout<<"choose a valid option, if your choice is not from the choice you can text me what you ate <3\n";
        break;
        return 0;
    }
    cout<<"***************************************************\n";
    cout<<"BONUS\n"<<"if you have ate anything extra with 3 things mentioned above then you get some extra points!!";
    cout<<"matlab for example you ate burger at the time between your lunch and dinner and ate your lunch and dinner as well\n";
    cout<<"if you did so TYPE Y for yes and N for no (type in capitals please!)\n";
    cout<<"Did you ate anything extra?";
    cin>>extra;
    switch(extra){
        case 'Y':
        ep=5;
        cout<<"YAYYYY ! you earned extra 5 points <3\n";
        break;
        case 'N':
        ep=0;
        cout<<"Its fine , bhuk nai hogi toh kon extra khaiga nw at all <3\n";
        break;
        default:
        ep=0;
        cout<<"Bola na type in capitals hehe\n";
        break;
        return 0;
    }
    cout<<"**********************NEXT****************************\n";
    cout<<"Tell me how much water you drank\n";
    cout<<"Try to keep a track of it hehe\n"<<"So how much water you drank?\n";
    cout<<"1. 0-1 litres\n"<<"2. 1-2 litres\n"<<"3. 2-3 litres\n"<<"4. 3-4 litres\n";
    cout<<"Enter your choice: \n";
    cin>>water;
    switch(water){
        case 1:
        ws=1;
        cout<<"Babe that is very poor , please try to drink more water , ho sake toh abhi jao pilo thoda paani\n";
        cout<<"*********POINTS EARNED "<<ws<<"*********\n";
        break;
        case 2:
        ws=2;
        cout<<"This good but like you need more wotah. Kal try krna you drink bas a lil more\n";
        cout<<"*********POINTS EARNED "<<ws<<"*********\n";
        break;
        case 3:
        ws=3;
        cout<<"Aye thats good , you drank good amount of water keep it up !\n";
        cout<<"*********POINTS EARNED "<<ws<<"*********\n";
        break;
        case 4:
        ws=5;
        cout<<"HEHE excellent work sweetie , you drank more than enough water . This much amount of water improves digestion , body health and skin ! great work!!\n";
        cout<<"*********POINTS EARNED "<<ws<<"*********\n";
        break;
        default:
        cout<<"choose a valid option please\n";
        return 0;
    }
    cout<<"**********************NEXT****************************\n";
    cout<<"HEHE HOW MUCH DID YOU STUDY\n";
    cout<<"1. 0-1 hours\n"<<"2. 1-2 hours\n"<<"3. 2-3 hours\n"<<"4. 3+ hours\n";
    cout<<"Enter your choice: \n";
    cin>>sss;
    switch(sss){
        case 1:
        sa=1;
        cout<<"Hehe it is fine in normal college day, but if you are in exam times abhi rest aache se and kal do more study\n";
        cout<<"POINTS EARNED : "<<sa;
        break;
        case 2:
        sa=2;
        cout<<"Aye thats great , you definately did became producitve today yayy !\n";
        cout<<"POINTS EARNED : "<<sa;
        break;
        case 3:
        sa=4;
        cout<<"Babeuu i am so proud if youu ! You studying motivates me tooo hehe\n";
        cout<<"POINTS EARNED : "<<sa;
        break;
        case 4:
        sa=5;
        cout<<"AYOO thats AWESOMEEE you did soooo great and became soooooo productive , i am hell lottta proud of you today (i always am proud of you tho hehe)\n";
        cout<<"POINTS EARNED : "<<sa;
        break;
        default:
        cout<<"choose a valid option";
        break;
        return 0;
    }
    cout<<"**********************NEXT****************************\n";
    cout<<"WE HAVE NOW HOW MUCH GAMES YOU PLAYED?\n";
    cout<<"1. 0-1 hours\n"<<"2. 1-2 hours\n"<<"3. 2-3 hours\n"<<"4. 3+ hours\n";
    cout<<"Enter your choice: \n";
    cin>>ga;
    switch(ga){
        case 1:
        gas=5;
        cout<<"Hehe itna kam kyo khele ? you can go play thoda more now , naito kuch saath khete cmon\n";
        cout<<"POINTS EARNED : "<<gas;
        break;
        case 2:
        gas=4;
        cout<<"Oh did you enjoyed playing? aur khelna ? tell me what you think hehe\n";
        cout<<"POINTS EARNED : "<<gas;
        break;
        case 3:
        gas=3;
        cout<<"Hehe how was your gaming session , what what you did ? lets talk about it !\n";
        cout<<"POINTS EARNED : "<<gas;
        break;
        case 4:
        gas=2;
        cout<<"Hehe bahut khela na aaj , you must be tired aisa continuously nai khelneka aaram aaram leke khelneka , now rest chalo\n";
        cout<<"POINTS EARNED : "<<gas;
        break;
        default:
        cout<<"choose a valid option";
        break;
        return 0;
    }
    cout<<"*********NOW FOR THE FINAL SCORE !!***************\n";
    cout<<"Sleep mein you earned : "<<ss<<"\n";
    cout<<"Breakfast mein you earned : "<<bfs<<"\n";
    cout<<"Lunch mein you earned : "<<lfs<<"\n";
    cout<<"Dinner mein you earned : "<<dfs<<"\n";
    cout<<"Water mein you earned : "<<ws<<"\n";
    cout<<"Studies mein you earned : "<<sa<<"\n";
    cout<<"Gaming mein you earned : "<<gas<<"\n";
    cout<<"Plus an extra : "<<ep<<"\n";
    cout<<"****************************************************\n";
    cout<<" SOOO VAISH'S TODAYS SCORE IS !\n";
    ts=ss+bfs+lfs+dfs+ws+sa+gas+ep;
    cout<<ts<<"/35 !\n";
    cout<<"YAYYYYY !!\n"<<"NOW SEND ME YOUR SCORE SO THAT I CAN ADD IT IN THE SHEET SO WE CAN HAVE A TRACK OF IT THE WHOLE YEAR <3";

}