/*
 * Task: Coin Combinations I
 * Link: https://cses.fi/problemset/task/1635
 * Topic: Dynamic Programming / 1D DP (Permutations / Ordered Coin Change)
 * Complexity: O(N * X) time, O(X) auxiliary space
 * Note: Implemented in Java to bypass Python's bytecode overhead for 10^8 operations limit.
 */

import java.io.*;
import java.util.*;

public class CoinCombinations {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());

        int[] coins = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(coins);

        int[] dp = new int[target + 1];
        dp[0] = 1;
        int MOD = 1000000007;

        for (int i = coins[0]; i <= target; i++) {
            long s = 0;
            for (int c : coins) {
                if (c > i) break;
                s += dp[i - c];
            }
            dp[i] = (int)(s % MOD);
        }
        System.out.println(dp[target]);
    }
}