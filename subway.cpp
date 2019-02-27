#include <iostream>
using namespace std;

//地铁1号线，2号线，13号线，10号线地铁站名数组 
const string stopName[94]={"pingguoyuan","gucheng","bajao amusement park","babaoshan","yuquanlu","wukesong","wangshoulu","gongzhufen","military museum","muxidi","nanlishilu","fuxingmen","xidan","tiananmen west","tiananmen east","wangfujing","dongdan","jianguomen","yong'anli","guomao","dawanglu","sihui","sihuieast",//一号线 
							"xizhimen","jishuitan","guoloudajie","andingmen","yonghegong","dongzhimen","dongsishitiao","chaoyangmen","beijing railway station","chongwenmen","qianmen","hepingmen","xuanwumen","changchunjie","fuchengmen","chegongzhuang",//二号线 
							"dazhongsi","zhichunlu","wudaokou","shangdi","xierqi","longze","huilongguan","huoying","lishuiqiao","beiyuan","wangjing west","shaoyaoju","guangximen","liufang",//十三号线 
							"huoqiying","bagou","suzhoujie","haidianhuangzhuang","zhichunli","xitucheng","mudanyuan","jiandemen","beitucheng","anzhenmen","huixinxijie nankou","taiyanggong","sanyuanqiao","liangmaqiao","agricultural exhibition center","tuanjiehu","hujialou","jintaixizhao","shuangjing","jinsong","panjiayuan","shilihe","fenzhongsi","chengshousi","songjiazhuang","shiliuzhuang","dahongmen","jiaomen east","jiaomen west","caoqiao","jijiamiao","shoujingmao","fengtai railway station","niwa","xiju","liuliqiao","lianhuaqiao","xidiaoyutai","cishousi","chedaogou","changchunqiao"} ;//十号线 

const int maxnum = 95;     //限制索引 
const int n=94;  //四条线地铁站数 
const int maxint = 999999;   //定义无穷大 
  
int p, q;       // p表示起点索引，q表示终点suoyin 
int dist[maxnum];     // 表示当前点到源点的最短路径长度
int path[maxnum];     // 记录当前点的前一个结点
int c[maxnum][maxnum];   // 联结矩阵，记录图的两点间路径长度


//Dijkstra算法 
void Dijkstra(int v, int *dist, int *path, int c[maxnum][maxnum])     //v表示起点   
{
	bool s[maxnum];    // 判断是否已存入该点到S集合中
	
	for (int i = 1; i <= n; i++)
	{
		dist[i] = c[v][i];
		s[i] = 0;     // 初始都未用过该点
		
		if (dist[i] < maxint)
			path[i] = v;
		else
			path[i] = 0;
	}
	
	dist[v] = 0;
	s[v] = 1;

	for (int i = 2; i <= n; i++)
	{
		int distance = maxint;
		int k = v;
		
		// 找出当前未使用的点j的dist[j]最小值
		for (int j = 1; j <= n; j++)
		if ((!s[j]) && dist[j]<distance)
		{
			k = j;              // k保存当前邻接点中距离最小的点的号码
			distance = dist[j];
		}
		
		s[k] = 1;    // 表示k点已存入S集合中

		// 更新dist
		for (int j = 1; j <= n; j++)
		if ((!s[j]) && c[k][j]!=maxint)
		{
			int newdist = dist[k] + c[k][j];
			if (newdist < dist[j])
			{
				dist[j] = newdist;
				path[j] = k;
			}
		}
	}
}


//初始化函数 
void init()
{
	for (int i = 1; i <= n; i++)
		path[i] = 0;
		
	// 初始化c[][]为maxint
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j){
			if(i==j) c[i][j]=0;
			else c[i][j] = maxint;
		}
			

	//一号线
	c[1][2] = c[2][1] = 2606;
	c[2][3] = c[3][2] = 1921;
	c[3][4] = c[4][3] = 1953;
	c[4][5] = c[5][4] = 1479;
	c[5][6] = c[6][5] = 1810;
	c[6][7] = c[7][6] = 1778;
	c[7][8] = c[8][7] = 1313;
	c[8][9] = c[9][8] = 1172;
	c[9][10] = c[10][9] = 1166;
	c[10][11] = c[11][10] = 1291;
	c[11][12] = c[12][11] = 424;
	c[12][13] = c[13][12] = 1590;
	c[13][14] = c[14][13] = 1217;
	c[14][15] = c[15][14] = 925;
	c[15][16] = c[16][15] = 852;
	c[16][17] = c[17][16] = 774;
	c[17][18] = c[18][17] = 1230;
	c[18][19] = c[19][18] = 1377;
	c[19][20] = c[20][19] = 790;
	c[20][21] = c[21][20] = 1385;
	c[21][22] = c[22][21] = 1673;
	c[22][23] = c[23][22] = 1714;
	//二号线
	c[24][39] = c[39][24] = 909;
	c[38][39] = c[39][38] = 960;
	c[12][38] = c[38][12] = 1832;
	c[12][37] = c[37][12] = 1234;
	c[36][37] = c[37][36] = 929;
	c[35][36] = c[36][35] = 851;
	c[34][35] = c[35][34] = 1171;
	c[33][34] = c[34][33] = 1634;
	c[32][33] = c[33][32] = 1023;
	c[18][32] = c[32][18] = 945;
	c[18][31] = c[31][18] = 1763;
	c[31][30] = c[30][31] = 1027;
	c[30][29] = c[29][30] = 824;
	c[29][28] = c[28][29] = 2228;
	c[28][27] = c[27][28] = 794;
	c[27][26] = c[26][27] = 1237;
	c[26][25] = c[25][26] = 1766;
	c[25][24] = c[24][25] = 1899;
	//十三号线
	c[24][40] = c[40][24] = 2839;
	c[40][41] = c[41][40] = 1206;
	c[41][42] = c[42][41] = 1829;
	c[42][43] = c[43][42] = 4866;
	c[43][44] = c[44][43] = 2538;
	c[44][45] = c[45][44] = 3623;
	c[45][46] = c[46][45] = 1423;
	c[46][47] = c[47][46] = 2110;
	c[47][48] = c[48][47] = 4785;
	c[48][49] = c[49][48] = 2272;
	c[49][50] = c[50][49] = 6720;
	c[50][51] = c[51][50] = 2152;
	c[51][52] = c[52][51] = 1110;
	c[52][53] = c[53][52] = 1135;
	c[53][29] = c[29][53] = 1769;
	//十号线
	c[54][55] = c[55][54] = 1495;
	c[55][56] = c[56][55] = 1110;
	c[56][57] = c[57][56] = 950;
	c[57][58] = c[58][57] = 975;
	c[41][58] = c[58][41] = 1058;
	c[59][41] = c[41][59] = 1101;
	c[59][60] = c[60][59] = 1330;
	c[60][61] = c[61][60] = 973;
	c[61][62] = c[62][61] = 1100;
	c[62][63] = c[63][62] = 1020;
	c[63][64] = c[64][63] = 982;
	c[64][52] = c[52][64] = 1712;
	c[52][65] = c[65][52] = 1003;
	c[65][66] = c[66][65] = 1759;
	c[66][67] = c[67][66] = 1506;
	c[67][68] = c[68][67] = 914;
	c[68][69] = c[69][68] = 853;
	c[69][70] = c[70][69] = 1149;
	c[70][71] = c[71][70] = 734;
	c[71][20] = c[20][71] = 835;
	c[20][72] = c[72][20] = 1759;
	c[72][73] = c[73][72] = 1006;
	c[73][74] = c[74][73] = 1021;
	c[74][75] = c[75][74] = 1097;
	c[75][76] = c[76][75] = 1804;
	c[76][77] = c[77][76] = 1058;
	c[77][78] = c[78][77] = 1677;
	c[78][79] = c[79][78] = 1269;
	c[79][80] = c[80][79] = 1244;
	c[80][81] = c[81][80] = 1130;
	c[81][82] = c[82][81] = 1254;
	c[82][83] = c[83][82] = 1688;
	c[83][84] = c[84][83] = 1547;
	c[84][85] = c[85][84] = 1143;
	c[85][86] = c[86][85] = 1717;
	c[86][87] = c[87][86] = 954;
	c[87][88] = c[88][87] = 749;
	c[88][89] = c[89][88] = 1584;
	c[89][90] = c[90][89] = 2392;
	c[90][8] = c[8][90] = 1016;
	c[8][91] = c[91][8] = 2386;
	c[91][92] = c[92][91] = 1214;
	c[92][93] = c[93][92] = 1590;
	c[93][94] = c[94][93] = 1205;
	c[94][54] = c[54][94] = 961;


	for (int i = 1; i <= n; ++i)
		dist[i] = maxint;
}


//费用计算 
int money()
{
	int money; 
	if(dist[q]==0) money=9;
	else if (dist[q]/1000 < 6&&dist[q]/1000>0) money=3;
	else if (dist[q]/1000 >= 6 && dist[q] / 1000  < 12)  money=4;
	else if (dist[q]/1000 >= 12 && dist[q] / 1000  < 22)  money=5;
	else if (dist[q]/1000 >= 22 && dist[q] / 1000 < 32)  money=6;
	else if (dist[q]/1000 >= 32) money=6+(dist[q]/1000-32)/20;
	return money;
}


int main()
{
	init();   //初始化 
	string start,end;    //起点与终点名 

	//输入起点与终点名 
	getline(cin,start,';');
	getline(cin,end);


	//地铁名匹配相应索引 
	for(int i=0;i<94;i++){
		if(start==stopName[i]){
			p=i+1;
			break;			
		}	
	} 
	for(int i=0;i<94;i++){
		if(end==stopName[i]){
			q=i+1;
			break;
		}	
	} 
	
	//计算路径算法 
	Dijkstra(p, dist, path, c);

	//输出结果 
	
	cout<<money();	
}              
