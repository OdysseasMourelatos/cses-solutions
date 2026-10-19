/*
 * Task: Coin Combinations II
 * Link: https://cses.fi/problemset/task/1636
 * Topic: Dynamic Programming / 1D DP (Combinations / Unordered)
 * Complexity: O(N * X) time, O(X) auxiliary space
 */

import java.io.*;
import java.util.*;

public class CoinCombinationsII {
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

        for (int c : coins) {
            for (int i = c; i <= target; i++) {
                dp[i] = (dp[i] + dp[i - c]) % MOD;
            }
        }
        System.out.println(dp[target]);
    }
}