#define pi pair<int, string>
#define pii pair<int, pi>
#define piii pair<int, pi>
#define piiii pair<int, piii>
#include<iostream>
#include<bits/stdc++.h>
	using namespace std;
priority_queue<pi, vector<pi>, greater<pi>> Q;
priority_queue<pi, vector<pi>, greater<pi>> temp;
map<string, int> visit;
map<pi, vector<pi>> graph;
map<string, string> revert;
string start, stop;
int BestFirstSearch(string root, int a){
	Q.push(make_pair(a,root));
	visit[root] = 1;
	
	while(!Q.empty()){
		pi x = Q.top();
		Q.pop();
		cout << setw(10) << x.second << "-" << to_string(x.first) << setw(8) << " |";
		if(x.second == stop){
			cout << "\n found \n";
			return 1;
		}		
		string str = "";
		for(auto i: graph[x]){
			str += " " + i.second + "-" + to_string(i.first) + " ";
			if(visit.find(i.second) == visit.end()){
				revert[i.second] = x.second;
				Q.push(i);
				visit[i.second] = 1;
			}
		}
		cout << str << setw(42 - str.size()) << " |";
		temp = Q;
		while(!temp.empty()){
			cout << temp.top().second << "-" << temp.top().first << " ";
			temp.pop();
		}
		cout << endl;
	}
	return 0;
}
void printPath(string des){
	cout << revert[des] << (revert[des]== start?" " : " <- ");
	while(revert.find(revert[des]) != revert.end()){
		printPath(revert[des]);
		return;
	}
}
void solve(){
int n;  // s? d?nh
	cin >> n;
	cout<<setw(20)<<"Phat trien trang thai"<<setw(20)<<"Trang thai ke"<<setw(40)<<"Danh Sach L"<<endl;
	cout<<"=================================================================================="<<endl;
	for(int i = 0; i < n ; i++){
		int a, c; // a la so canh ke , c la trong so
		string b; // b la ten dinh
		cin >> a >> b >> c;
		for(int j = 0; j < a; j++){
			string x; // x la ten dinh ke ben danh sach L
			int d; // d la trong so 
			cin >> x >> d;
			graph[make_pair(c, b)].push_back(make_pair(d, x)); // danh sach ke cua moi dinh voi dinh va trong so
		}		
	}
	cin >> start >> stop;
	int found = BestFirstSearch(start, 20);
	if(found){
		cout << stop << " <- ";	
		printPath(stop);
	}else{
		cout << "Not Found";
	}
}
      
int main() {
	freopen("input_BestFirstSearch.txt", "r", stdin);
	freopen("output_BestFirstSearch.txt", "w", stdout);
	solve();
	return 0;

}
