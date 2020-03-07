#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class TrieNode
{
public:
    unordered_map<char, TrieNode *> children;
    bool is_word = false;
};

class Trie
{
public:
    void insert(string word);
    bool search(string word);
    bool starts_with(string prefix);

private:
    TrieNode root;
};

/**
 * Inserts a word into the trie.
 */
void Trie::insert(string word)
{
    TrieNode *curr = &root;
    for (auto c : word)
    {
        if (!curr->children.count(c))
            curr->children[c] = new TrieNode();
        curr = curr->children[c];
    }
    curr->is_word = true;
}

/**
 * Determines if word is in the trie.
 */
bool Trie::search(string word)
{
    TrieNode *curr = &root;
    for (auto c : word)
    {
        if (!curr->children.count(c))
            return false;
        curr = curr->children[c];
    }
    return curr->is_word;
}

/**
 * Determines if there is any word in the trie that starts with the
 * given prefix.
 */
bool Trie::starts_with(string prefix)
{
    TrieNode *curr = &root;
    for (auto c : prefix)
    {
        if (!curr->children.count(c))
            return false;
        curr = curr->children[c];
    }
    return true;
}