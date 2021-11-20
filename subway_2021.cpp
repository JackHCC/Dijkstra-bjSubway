#include <iostream>
#include <string>
using namespace std;

//地铁1号线，2号线，4号线，5号线地铁站名数组 
const string STOPARRAY[68] = { "pingguoyuan","gucheng","bajiao amusement park","babaoshan","yuquanlu","wukesong","wanshoulu","gongzhufen","military museum","muxidi","nanlishilu","fuxingmen","xidan","tian'anmen west","tian'anmen east","wangfujing","dongdan","jianguomen","yong'anli","guomao","dawanglu","sihui","sihui east","gaobeidian","communication university of china","shuangqiao","guaanzhuang","baliqiao","tongzhou beiyuan","guoyuan","jiukeshu","liyuan","linheli","tuqiao","huazhuang","huanqiudujiaqu",//一号线 
							"xizhimen","jishuitan","guloudajie","andingmen","yonghegong lama temple","dongzhimen","dongsishitiao","chaoyangmen","jianguomen","beijing railway station","chongwenmen","qianmen","hepingmen","xuanwumen","changchunjie","fuxingmen""fuchengmen","chegongzhuang",//二号线 
							"xizhimen","xinjiekou","ping'anli","xisi","lingjinghutong","xidan","xuanwumen",//四号线 
							"yonghegong lama temple","beixinqiao","zhangzizhonglu","dongsi","dengshikou","dongdan","chongwenmen" };//五号线 

const int MAXINDEX = 69;     //限制索引 
const int STOPNUM = 68;  //四条线地铁站数 
const int INF = 999999;   //定义无穷大 

int startIndex, endIndex;       // p表示起点索引，q表示终点索引 
int dist[MAXINDEX];     // 表示当前点到源点的最短路径长度
int path[MAXINDEX];     // 记录当前点的前一个结点
int Matrix[MAXINDEX][MAXINDEX];   // 联结矩阵，记录图的两点间路径长度


//Dijkstra算法 
void Dijkstra(int start, int* dist, int* path, int matrix[MAXINDEX][MAXINDEX])     //start表示起点   
{
	bool visited[MAXINDEX];    // 判断是否以访问节点

	for (int i = 1; i <= STOPNUM; i++)
	{
		dist[i] = matrix[start][i];
		visited[i] = 0;     // 初始都未用过该点

		if (dist[i] < INF)
			path[i] = start;
		else
			path[i] = 0;
	}

	dist[start] = 0;
	visited[start] = 1;

	for (int i = 2; i <= STOPNUM; i++)
	{
		int distance = INF;
		int k = start;

		// 找出当前未使用的点j的dist[j]最小值
		for (int j = 1; j <= STOPNUM; j++)
			if ((!visited[j]) && dist[j] < distance)
			{
				k = j;              // k保存当前邻接点中距离最小的点的号码
				distance = dist[j];
			}

		visited[k] = 1;    // 表示k点已存入visited集合中

		// 更新dist
		for (int j = 1; j <= STOPNUM; j++)
			if ((!visited[j]) && matrix[k][j] != INF)
			{
				int newdist = dist[k] + matrix[k][j];
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
	for (int i = 1; i <= STOPNUM; i++)
		path[i] = 0;

	// 初始化matrix[][]为INF
	for (int i = 1; i <= STOPNUM; ++i)
		for (int j = 1; j <= STOPNUM; ++j) {
			if (i == j) Matrix[i][j] = 0;
			else Matrix[i][j] = INF;
		}


	//一号线
	Matrix[1][2] = Matrix[2][1] = 2606;//苹果园开端
	Matrix[2][3] = Matrix[3][2] = 1921;
	Matrix[3][4] = Matrix[4][3] = 1953;
	Matrix[4][5] = Matrix[5][4] = 1479;
	Matrix[5][6] = Matrix[6][5] = 1810;
	Matrix[6][7] = Matrix[7][6] = 1778;
	Matrix[7][8] = Matrix[8][7] = 1313;
	Matrix[8][9] = Matrix[9][8] = 1172;
	Matrix[9][10] = Matrix[10][9] = 1166;
	Matrix[10][11] = Matrix[11][10] = 1291;
	Matrix[11][12] = Matrix[12][11] = 424;
	Matrix[12][13] = Matrix[13][12] = 1590;
	Matrix[13][14] = Matrix[14][13] = 1217;
	Matrix[14][15] = Matrix[15][14] = 925;
	Matrix[15][16] = Matrix[16][15] = 852;
	Matrix[16][17] = Matrix[17][16] = 774;
	Matrix[17][18] = Matrix[18][17] = 1230;
	Matrix[18][19] = Matrix[19][18] = 1377;
	Matrix[19][20] = Matrix[20][19] = 790;
	Matrix[20][21] = Matrix[21][20] = 1385;
	Matrix[21][22] = Matrix[22][21] = 1673;
	Matrix[22][23] = Matrix[23][22] = 1714;
	Matrix[23][24] = Matrix[24][23] = 1375;
	Matrix[24][25] = Matrix[25][24] = 2002;
	Matrix[25][26] = Matrix[26][25] = 1894;
	Matrix[26][27] = Matrix[27][26] = 1912;
	Matrix[27][28] = Matrix[28][27] = 1763;
	Matrix[28][29] = Matrix[29][28] = 1700;
	Matrix[29][30] = Matrix[30][29] = 1465;
	Matrix[30][31] = Matrix[31][30] = 990;
	Matrix[31][32] = Matrix[32][31] = 1225;
	Matrix[32][33] = Matrix[33][32] = 1257;
	Matrix[33][34] = Matrix[34][33] = 776;
	Matrix[34][35] = Matrix[35][34] = 2238;
	Matrix[35][36] = Matrix[36][35] = 1863;
	//二号线全部进行修改
	Matrix[13][52] = Matrix[52][13] = 0;//复兴门一号线二号线换乘
	Matrix[19][45] = Matrix[45][19] = 0;//建国门一号线二号线换乘
	Matrix[37][55] = Matrix[55][37] = 0;//西直门二号线四号线换乘
	Matrix[50][60] = Matrix[60][50] = 0;//宣武门二号线四号线换乘
	Matrix[37][36] = Matrix[36][37] = 1899;//西直门开端
	Matrix[38][37] = Matrix[37][38] = 1766;
	Matrix[39][38] = Matrix[38][39] = 1237;
	Matrix[40][39] = Matrix[39][40] = 794;
	Matrix[41][40] = Matrix[40][41] = 2228;
	Matrix[42][41] = Matrix[41][42] = 824;
	Matrix[43][42] = Matrix[42][43] = 1027;
	Matrix[44][43] = Matrix[43][44] = 1763;
	Matrix[45][44] = Matrix[44][45] = 945;
	Matrix[46][45] = Matrix[45][46] = 1023;
	Matrix[47][46] = Matrix[46][47] = 1634;
	Matrix[48][47] = Matrix[47][48] = 1171;
	Matrix[49][48] = Matrix[48][49] = 851;
	Matrix[50][49] = Matrix[49][50] = 929;
	Matrix[51][50] = Matrix[50][51] = 1234;
	Matrix[52][51] = Matrix[51][52] = 1832;
	Matrix[53][52] = Matrix[52][53] = 960;
	Matrix[54][53] = Matrix[53][54] = 909;
	Matrix[54][37] = Matrix[37][53] = 0;
	//四号线
	Matrix[60][13] = Matrix[13][60] = 0;//西单四号线一号线转站
	Matrix[55][56] = Matrix[56][55] = 1025;//西直门开端
	Matrix[56][57] = Matrix[57][56] = 1100;
	Matrix[57][58] = Matrix[58][57] = 1100;
	Matrix[58][59] = Matrix[59][58] = 869;
	Matrix[59][60] = Matrix[60][59] = 1011;
	Matrix[60][61] = Matrix[61][60] = 815;
	//五号线
	Matrix[62][41] = Matrix[41][62] = 0;//雍和宫二号线五号线转站
	Matrix[68][47] = Matrix[47][68] = 0;//崇文门二号线五号线转站
	Matrix[67][17] = Matrix[17][67] = 0;//东单一号线五号线转站
	Matrix[62][63] = Matrix[63][62] = 1495;//雍和宫开端
	Matrix[63][64] = Matrix[64][63] = 1110;
	Matrix[64][65] = Matrix[65][64] = 950;
	Matrix[65][66] = Matrix[66][65] = 975;
	Matrix[66][67] = Matrix[67][66] = 1058;
	Matrix[67][68] = Matrix[68][67] = 1101;

	for (int i = 1; i <= STOPNUM; ++i)
		dist[i] = INF;
}


//费用计算 
int money()
{
	int money;
	if (dist[endIndex] / 1000 < 6 && dist[endIndex] / 1000 >= 0) money = 3;
	else if (dist[endIndex] / 1000 >= 6 && dist[endIndex] / 1000 < 12)  money = 4;
	else if (dist[endIndex] / 1000 >= 12 && dist[endIndex] / 1000 < 22)  money = 5;
	else if (dist[endIndex] / 1000 >= 22 && dist[endIndex] / 1000 < 32)  money = 6;
	else if (dist[endIndex] / 1000 >= 32) money = 6 + (dist[endIndex] / 1000 - 32) / 20;
	return money;
}

int getIndexFromArray(string stopName) {
	int index;
	for (int i = 0; i < MAXINDEX; i++) {
		if (stopName == STOPARRAY[i]) {
			index = i + 1;
			break;
		}
	}
	return index;
}


int main()
{
	init();   //初始化 
	string start, end;    //起点与终点名 

	//输入起点与终点名 
	getline(cin, start, ';');
	getline(cin, end);

	startIndex = getIndexFromArray(start);
	endIndex = getIndexFromArray(end);

	//计算路径算法 
	Dijkstra(startIndex, dist, path, Matrix);

	//输出结果 
	cout << money();
}



