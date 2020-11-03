/*
 * Problem link: https://leetcode.com/problems/lru-cache/
 * Optimized for O(1), Get/Set Option
 * */
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.map = new Map();
    this.capacity = capacity;
};
/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if(this.map.has(key)){
        const value = this.map.get(key);
        this.map.delete(key);
        this.map.set(key, value)
        return this.map.get(key);
    }else{
        return -1;
    }
};
/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if(this.map.size < this.capacity){
        this.map.set(key, value);
    } else {
        this.map.delete(this.map.keys().next().value);
        this.map.set(key, value);
    }
};
/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */