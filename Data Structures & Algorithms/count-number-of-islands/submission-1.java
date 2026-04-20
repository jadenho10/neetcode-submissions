class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1'){
                    if (dfs(i, j, grid)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
    private boolean dfs(int i, int j, char[][] grid) {
        if (i < 0 || j < 0 || i > grid.length - 1 || j > grid[0].length - 1 || grid[i][j] != '1')  
            return false;
        grid[i][j] = 0;
        dfs(i + 1, j, grid);
        dfs(i, j + 1, grid);
        dfs(i - 1, j, grid);
        dfs(i, j - 1, grid);
        return true;
    }
}
