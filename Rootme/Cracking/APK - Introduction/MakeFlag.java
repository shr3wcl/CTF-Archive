public class MakeFlag{
    public static String makeFlag(String s) {
        String a = "" + s.charAt(5);
        String _b = s.charAt(2) + "";
        for (int s_ = 0; s_ < s.length(); s_++) {
            String b = _b.substring(_b.length() - s_) + _b.substring(s_);
            String _b2 = s_ >= 3 ? _b + s.charAt(s_ - 3) + "" : _b + s.charAt(s.length() - (3 - s_)) + "";
            if (s_ >= _b2.length()) {
                _b = _b2 + s.charAt(s_ - _b2.length()) + "";
            } else if (s.length() >= _b2.length() - s_) {
                _b = _b2 + s.charAt(s.length() - (_b2.length() - s_)) + "";
            } else {
                _b = _b2 + s.charAt(s.length() - ((_b2.length() - s_) - s.length())) + "";
            }
            a = a + b.charAt((((s.length() + _b.length()) * s_) + _b.length()) % b.length());
        }
        return a.substring(0, 2) + s.charAt(3) + a.charAt(3) + '0' + a.substring(5, 7);
    }

    public static void main(String[] args){
        String seed = "1dndr@";
        String flag = makeFlag(seed);
        System.out.print("Flag is: " + flag);
    }
}