public class ReplaceWords648 {
    public String replaceWords(List<String> dictionary, String sentence) {
        String result = "";
        String[] splitSentence = sentence.split(" ");
        for (String word:splitSentence) {
            result += " " + getRoot(word, dictionary);
        }
        return result.substring(1,result.length());
    }

    public String getRoot(String word, List<String> dictionary) {
        int len = word.length();
        String rootResult = "";
        for (String root:dictionary) {
            if (word.length() < root.length())
                continue;
            if ((word.substring(0,root.length())).equals(root) && root.length() < len){
                rootResult = root;
                len = root.length();
            }
        }
        if (rootResult.equals(""))
            return word;
        return rootResult;
    }
}
