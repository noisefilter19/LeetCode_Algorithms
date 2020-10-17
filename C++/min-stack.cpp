class MinStack {
public:
    /** initialize your data structure here. */
    vector<int> a, b;
    MinStack() {
        a = b = {};
    }
    
    void push(int x) {
        a.push_back(x);
        if(b.empty()) b.push_back(x);
        else {
            int newMin = min(x, *b.rbegin());
            b.push_back(newMin);
        }
    }
    
    void pop() {
        a.pop_back();
        b.pop_back();
    }
    
    int top() {
        return *a.rbegin();
    }
    
    int getMin() {
       return *b.rbegin();
    }
};
