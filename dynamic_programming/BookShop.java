/*
 * Task: Book Shop
 * Link: https://cses.fi/problemset/task/1158
 * Topic: Dynamic Programming / 0-1 Knapsack (Space Optimized)
 * Complexity: O(N * X) time, O(X) auxiliary space
 * Strategy: Reverse 1D iteration to enforce each item being selected at most once.
 */

import java.io.*;
import java.util.*;

public class BookShop {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int books = Integer.parseInt(st.nextToken());
        int max_price = Integer.parseInt(st.nextToken());

        int[] prices = new int[books];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < books; i++) {
            prices[i] = Integer.parseInt(st.nextToken());
        }

        int[] pages = new int[books ];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < books; i++) {
            pages[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[max_price + 1];

        for (int i = 0; i < books; i++) {
            for (int j = max_price; j >= prices[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - prices[i]] + pages[i]);
            }
        }

        System.out.println(dp[max_price]);
    }
}