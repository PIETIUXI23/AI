#include<bits/stdc++.h>
using namespace std;
queue<string> Q;//hang doi 
queue<string> temp;//danh sach L
map<string, int> visit;//danh sach da tham
map<string, vector<string> > graph;// danh sach ke
map<string, string> revert;//chua trang thai di
string start, stop;//bat dau va ket thuc
int n;
int BFS(string root){
	Q.push(root);
	visit[root] = 1;
	while(!Q.empty()){
		string x = Q.front();
		Q.pop();
		cout << setw(10) << x << setw(10) << " |";
		if(x == stop){//da den diem can tim
			cout << "\n found \n";
			return 1;
		}
		string str = "";
		for(auto i: graph[x]){//tim trong danh sach ke cua dinh do
			str += " " + i + " ";
			if(visit.find(i) == visit.end()){//neu diem i chua duoc tham den
				revert[i] = x;//xac dinh diem dan den i la x
				Q.push(i);
				visit[i] = 1;				}
		}
		cout << str << setw(22 - str.size()) << " |";
		temp = Q;
		while(!temp.empty()){
			cout << temp.front().c_str() << " ";
			temp.pop();
		}
		cout << endl;
	}
	return 0;
}
void printPath(string des){//do nguoc tu dau
	cout << revert[des] << (revert[des]== start?" " : " <- ");
	while(revert.find(revert[des]) != revert.end()){//neu khong lap lai thi tiep tuc do
		printPath(revert[des]);
		return;
		}
}
void solve(){
	cin >> n;
	for(int i = 0; i < n ; i++){
		int a;//a la so canh ke, c la trong so
		string b;//b la ten dinh
		cin >> a >> b;
		for(int j = 0; j < a; j++){
			string x; //x la dinh ke
			// d la trong so, e la do dai canh
			cin >> x;
			graph[b].push_back(x);// graph la danh sach ke cua moi dinh
		}		
	}
	cin >> start >> stop;
	cout<<setw(20)<<"Phat trien trang thai"<<setw(20)<<"Trang thai ke"<<setw(20)<<"Danh Sach L"<<endl;
	cout<<"=================================================================================="<<endl;
	int found = BFS(start);
	if(found){
		cout << stop << " <- ";	
		printPath(stop);
	}else{
		cout << "Not Found";
	}
}
int main(){
	freopen("input_BreathFirstSearch.txt", "r", stdin);
	freopen("output_BreathFirstSearch.txt", "w", stdout);
	solve();
	return 0;
}

