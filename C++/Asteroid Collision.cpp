class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        int n = asteroids.size();
        stack<int>s;

        for (int i = 0; i < asteroids.size(); i++) {
            int x = asteroids[i];
            //Asteroids are moving in the negative direction
            if (x < 0) {
                //If the left of asteroids(stack topmost element) moving in the positive direction 
                //but having magnitude less than the current asteroids, then it will destroy it.
                while (!s.empty() && s.top() > 0 && abs(x) > s.top()) s.pop();

                //We will push current asteroid in only two condition
                //1)If current asteroid destroy all the previous asteroid----> means (Empty stack)
                //2)If current asteroid and rest of the asteroid are moving in the same direction (-ve)
                if (s.empty() || s.top() < 0) s.push(x);

                //if the current asteroid and the previous asteroid having the same magnitude, then both asteroid will destroy
                else if (abs(x) == s.top()) s.pop();
            }
            else {
                s.push(x);
            }
        }
        int len = s.size();
        vector<int>ans(len);
        int idx = len - 1;
        while (!s.empty()) {
            ans[idx--] = s.top();
            s.pop();
        }
        return ans;
    }
};
