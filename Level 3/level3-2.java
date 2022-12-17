import java.math.BigInteger;
import java.util.HashMap;

public class Solution {
    public static int solution(String x) {
        BigInteger d = new BigInteger(x);
        return solution_util(d).intValue();
    }

    // returns the nearest power of two with distance to it (mode=1: greater, mode=2: smaller)
    public static BigInteger[] np2(BigInteger x, boolean mode) {
        BigInteger ans;
        if (x.equals(BigInteger.ZERO)) ans = BigInteger.ONE;
        else {
            int a = x.bitLength();
            if (mode) {
                ans = BigInteger.ONE.shiftLeft(a);
            } else {
                ans = BigInteger.ONE.shiftLeft(a - 1);
            }
        }
        BigInteger[] res;
        if (x.compareTo(ans) < 0)
            res = new BigInteger[]{ans, ans.subtract(x)};
        else
            res = new BigInteger[]{ans, x.subtract(ans)};
        return res;
    }

    public static HashMap<BigInteger, BigInteger> mem = new HashMap<>();

    public static BigInteger solution_util(BigInteger n) {

        if (mem.get(n) != null) {
            return mem.get(n);
        }
        if (n.equals(BigInteger.ONE) || n.equals(BigInteger.ZERO))
            return BigInteger.ZERO;

        BigInteger[] g = np2(n, true);
        BigInteger[] s = np2(n, false);

        if (g[1].equals(BigInteger.ZERO)) {
            mem.put(g[0], BigInteger.valueOf(g[0].bitLength() - 1));
            return mem.get(g[0]);
        }
        if (s[1].equals(BigInteger.ZERO)) {
            mem.put(s[0], BigInteger.valueOf(s[0].bitLength() - 1));
            return mem.get(s[0]);
        }

        mem.put(s[0], solution_util(s[0]));
        mem.put(g[0], solution_util(g[0]));
        BigInteger p3;
        if (n.testBit(0)) { //odd
            mem.put(n.add(BigInteger.ONE).divide(BigInteger.TWO), solution_util(n.add(BigInteger.ONE).divide(BigInteger.TWO)));
            mem.put(n.subtract(BigInteger.ONE).divide(BigInteger.TWO), solution_util(n.subtract(BigInteger.ONE).divide(BigInteger.TWO)));

            p3 = mem.get(n.add(BigInteger.ONE).divide(BigInteger.TWO)).min(mem.get(n.subtract(BigInteger.ONE).divide(BigInteger.TWO))).add(BigInteger.TWO);
        } else {
            mem.put(n.divide(BigInteger.TWO), solution_util(n.divide(BigInteger.TWO)));
            p3 = mem.get(n.divide(BigInteger.TWO)).add(BigInteger.ONE);
        }

        return mem.get(s[0]).add(s[1]).min(mem.get(g[0]).add(g[1])).min(p3);
    }

    public static void main(String[] args) {
        System.out.println(solution("15"));
        // System.out.println(solution("8810822610936164971310313186837410979920845487103513753391774103243102068223177352981099669051998691571017216199257395100770106511811777970181031639433381503604515099981751017375420391010262899013210191009710751061310697915875296703511593837105386095035805664099443521005897473579112319491080101033829959826"));
    }
}
