#include <iostream>
#include <string>
using namespace std;

//����1���ߣ�2���ߣ�4���ߣ�5���ߵ���վ������ 
const string STOPARRAY[68] = { "pingguoyuan","gucheng","bajiao amusement park","babaoshan","yuquanlu","wukesong","wanshoulu","gongzhufen","military museum","muxidi","nanlishilu","fuxingmen","xidan","tian'anmen west","tian'anmen east","wangfujing","dongdan","jianguomen","yong'anli","guomao","dawanglu","sihui","sihui east","gaobeidian","communication university of china","shuangqiao","guaanzhuang","baliqiao","tongzhou beiyuan","guoyuan","jiukeshu","liyuan","linheli","tuqiao","huazhuang","huanqiudujiaqu",//һ���� 
							"xizhimen","jishuitan","guloudajie","andingmen","yonghegong lama temple","dongzhimen","dongsishitiao","chaoyangmen","jianguomen","beijing railway station","chongwenmen","qianmen","hepingmen","xuanwumen","changchunjie","fuxingmen""fuchengmen","chegongzhuang",//������ 
							"xizhimen","xinjiekou","ping'anli","xisi","lingjinghutong","xidan","xuanwumen",//�ĺ��� 
							"yonghegong lama temple","beixinqiao","zhangzizhonglu","dongsi","dengshikou","dongdan","chongwenmen" };//����� 

const int MAXINDEX = 69;     //�������� 
const int STOPNUM = 68;  //�����ߵ���վ�� 
const int INF = 999999;   //��������� 

int startIndex, endIndex;       // p��ʾ���������q��ʾ�յ����� 
int dist[MAXINDEX];     // ��ʾ��ǰ�㵽Դ������·������
int path[MAXINDEX];     // ��¼��ǰ���ǰһ�����
int Matrix[MAXINDEX][MAXINDEX];   // ������󣬼�¼ͼ�������·������


//Dijkstra�㷨 
void Dijkstra(int start, int* dist, int* path, int matrix[MAXINDEX][MAXINDEX])     //start��ʾ���   
{
	bool visited[MAXINDEX];    // �ж��Ƿ��Է��ʽڵ�

	for (int i = 1; i <= STOPNUM; i++)
	{
		dist[i] = matrix[start][i];
		visited[i] = 0;     // ��ʼ��δ�ù��õ�

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

		// �ҳ���ǰδʹ�õĵ�j��dist[j]��Сֵ
		for (int j = 1; j <= STOPNUM; j++)
			if ((!visited[j]) && dist[j] < distance)
			{
				k = j;              // k���浱ǰ�ڽӵ��о�����С�ĵ�ĺ���
				distance = dist[j];
			}

		visited[k] = 1;    // ��ʾk���Ѵ���visited������

		// ����dist
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


//��ʼ������ 
void init()
{
	for (int i = 1; i <= STOPNUM; i++)
		path[i] = 0;

	// ��ʼ��matrix[][]ΪINF
	for (int i = 1; i <= STOPNUM; ++i)
		for (int j = 1; j <= STOPNUM; ++j) {
			if (i == j) Matrix[i][j] = 0;
			else Matrix[i][j] = INF;
		}


	//һ����
	Matrix[1][2] = Matrix[2][1] = 2606;//ƻ��԰����
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
	//������ȫ�������޸�
	Matrix[13][52] = Matrix[52][13] = 0;//������һ���߶����߻���
	Matrix[19][45] = Matrix[45][19] = 0;//������һ���߶����߻���
	Matrix[37][55] = Matrix[55][37] = 0;//��ֱ�Ŷ������ĺ��߻���
	Matrix[50][60] = Matrix[60][50] = 0;//�����Ŷ������ĺ��߻���
	Matrix[37][36] = Matrix[36][37] = 1899;//��ֱ�ſ���
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
	//�ĺ���
	Matrix[60][13] = Matrix[13][60] = 0;//�����ĺ���һ����תվ
	Matrix[55][56] = Matrix[56][55] = 1025;//��ֱ�ſ���
	Matrix[56][57] = Matrix[57][56] = 1100;
	Matrix[57][58] = Matrix[58][57] = 1100;
	Matrix[58][59] = Matrix[59][58] = 869;
	Matrix[59][60] = Matrix[60][59] = 1011;
	Matrix[60][61] = Matrix[61][60] = 815;
	//�����
	Matrix[62][41] = Matrix[41][62] = 0;//Ӻ�͹������������תվ
	Matrix[68][47] = Matrix[47][68] = 0;//�����Ŷ����������תվ
	Matrix[67][17] = Matrix[17][67] = 0;//����һ���������תվ
	Matrix[62][63] = Matrix[63][62] = 1495;//Ӻ�͹�����
	Matrix[63][64] = Matrix[64][63] = 1110;
	Matrix[64][65] = Matrix[65][64] = 950;
	Matrix[65][66] = Matrix[66][65] = 975;
	Matrix[66][67] = Matrix[67][66] = 1058;
	Matrix[67][68] = Matrix[68][67] = 1101;

	for (int i = 1; i <= STOPNUM; ++i)
		dist[i] = INF;
}


//���ü��� 
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
	init();   //��ʼ�� 
	string start, end;    //������յ��� 

	//����������յ��� 
	getline(cin, start, ';');
	getline(cin, end);

	startIndex = getIndexFromArray(start);
	endIndex = getIndexFromArray(end);

	//����·���㷨 
	Dijkstra(startIndex, dist, path, Matrix);

	//������ 
	cout << money();
}



