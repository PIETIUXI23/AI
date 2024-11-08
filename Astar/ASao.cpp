#define pi pair<int, string>
#define pii pair<int, pi>
#define piii pair<int, pi>
#define piiii pair<int, piii>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
	priority_queue<piiii, vector<piiii>, greater<piiii>> Q;
	priority_queue<piiii, vector<piiii>, greater<piiii>> temp;
	map<string, int> visit;
	map<pi, vector<pii>> graph;
	map<string, string> revert;
	string start, stop;
	map<string, int> mups;

int ASao(string root, int a){
Q.push(make_pair(0, make_pair(0, make_pair(a, root))));
visit[root] = 1;
	
	while(!Q.empty()){
		piiii x = Q.top();
		Q.pop();
		cout << setw(10) << x.second.second.second << "-" << to_string(x.first) << setw(8) << " \t";
		if(x.second.second.second == stop){
			cout << "Trang thai ket thuc \n";
			return 1;
		}		
		int g = x.second.first;
		string str = "";
		for(auto i: graph[x.second.second]){
			int g1 = g + i.first;
			int f = g1 + i.second.first;
			str +=  "\t" + i.second.second + " ";
			str += "\t " + to_string(i.first) + " \t  " + to_string(i.second.first) + " \t  " + to_string(g1) + " \t " + to_string(f) + " \n\t\t\t "  ;
			revert[i.second.second] = x.second.second.second;
			Q.push(make_pair(f, make_pair(g1, i.second)));
		}
		
		cout <<str<< "";
		// in danh sach L
		temp = Q;
		cout<< "\t\t\t\t\t\t\t";
		while(!temp.empty()){
			cout <<temp.top().second.second.second << "-" << temp.top().first << " ";
			temp.pop();
		}
		cout << endl;
		cout <<"--------------------------------------------------------------------------------------------------------------------\n";
	}
	return 0;
}
void printPath(string des){
if (revert.find(des) != revert.end()) {
        printPath(revert[des]);
        cout << " -> ";
    }
    cout << des;
}
void printGraph(){
	for(auto i : graph){
		cout << i.first.second << " ";
		for(auto j : i.second){
			cout << j.second.second << " " << j.second.first << endl;
		}
		cout << endl;
	}
}
void solve(){
	int n;
	cin >> n;
		cout<<setw(10)<<"Phat trien trang thai | "<<setw(30)<<" Trang thai ke | k(u,v) | h(v)) | g(v) | f(v) |"<<setw(30)<<" Danh Sach L"<<endl;
	cout<<"============================================================================================================================="<<endl;
	for(int i =0; i<n ; i++){
		string a;
		int b;
		cin>>a>>b;
		mups[a]= b;
	}
	for(int i = 0; i < n ; i++){
		int a;
		string b;
		cin>>a>>b;
		auto c = mups.find(b);
		int h = c->second;
		for(int j = 0; j < a; j++){
			string d;
			int e;
			cin>>d>>e;
			auto l = mups.find(d);
			int x = l->second;
			graph[make_pair(h, b)].push_back(make_pair(e, make_pair(x, d)));
		}	
	}
	cin >> start >> stop;
	int found = ASao(start, 14);
if (found == 1) {
		    cout << "Found: ";
		    printPath(stop);
		    cout << endl;
		} else {
		    cout << "Not Found" << endl;
		}
}
int main() {

	freopen("C://Users//admin//Downloads//A//inputA.txt", "r", stdin);
	freopen("C://Users//admin//Downloads//A//outputA.txt", "w", stdout);
	solve();
	return 0;

}
