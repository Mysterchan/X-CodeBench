import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static final int[][] directions = new int[][] {
            new int[]{0, 1}, new int[]{0, -1},
            new int[]{1, 0}, new int[]{-1, 0}
    };

    public static void main(String[] args) throws IOException {
        final IOHandler ioHandler = new IOHandler();
        final int rows = Integer.parseInt(ioHandler.read());
        final int columns = Integer.parseInt(ioHandler.read());
        final char[][] board = new char[rows][columns];
        for (int rowNumber = 0; rowNumber < rows; ++rowNumber) {
            board[rowNumber] = ioHandler.read().toCharArray();
        }

        final Queue<Cell> bfsQueue = new ArrayDeque<>();
        for (int rowNumber = 0; rowNumber < rows; ++rowNumber) {
            for (int columnNumber = 0; columnNumber < columns; ++columnNumber) {
                if (board[rowNumber][columnNumber] == '#') {
                    bfsQueue.offer(new Cell(rowNumber, columnNumber));
                }
            }
        }

        while (!bfsQueue.isEmpty()) {
            final int length = bfsQueue.size();
            final List<Cell> whiteCells = new ArrayList<>();

            for (int index = 0; index < length; ++index) {
                final Cell currentCell = bfsQueue.poll();
                final int currentRowNumber = currentCell.rowNumber;
                final int currentColumnNumber = currentCell.columnNumber;
                board[currentRowNumber][currentColumnNumber] = '#';

                for (final int[] direction : directions) {
                    final int nextRowNumber = currentRowNumber + direction[0];
                    final int nextColumnNumber = currentColumnNumber + direction[1];
                    final Cell nextCell = new Cell(nextRowNumber, nextColumnNumber);

                    if (nextCell.isSafeCell(rows, columns) && board[nextRowNumber][nextColumnNumber] == '.') {
                        whiteCells.add(nextCell);
                    }
                }
            }

            for (final Cell whiteCell : whiteCells) {
                int blackCells = 0;

                for (final int[] direction : directions) {
                    final int nextRowNumber = whiteCell.rowNumber + direction[0];
                    final int nextColumnNumber = whiteCell.columnNumber + direction[1];
                    final Cell nextCell = new Cell(nextRowNumber, nextColumnNumber);

                    if (nextCell.isSafeCell(rows, columns) && board[nextRowNumber][nextColumnNumber] == '#') {
                        ++blackCells;
                    }
                }

                if (blackCells == 1) {
                    bfsQueue.offer(whiteCell);
                }
            }
        }

        int blackCells = 0;
        for (final char[] currentRow : board) {
            for (final char currentCell : currentRow) {
                if (currentCell == '#') {
                    ++blackCells;
                }
            }
        }
        ioHandler.write(blackCells + "\n");
        ioHandler.close();
    }

    private static final class Cell {
        private final int rowNumber;
        private final int columnNumber;

        public Cell(final int rowNumber, final int columnNumber) {
            this.rowNumber = rowNumber;
            this.columnNumber = columnNumber;
        }

        public boolean isSafeCell(final int rows, final int columns) {
            return rowNumber >= 0 && rowNumber < rows && columnNumber >= 0 && columnNumber < columns;
        }
    }

    private static final class IOHandler implements Closeable {
        private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        private final BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        private StringTokenizer tokenizer;

        public String read() throws IOException {
            while (Objects.isNull(tokenizer) || !tokenizer.hasMoreElements()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }

            return tokenizer.nextToken();
        }

        public void write(final String output) throws IOException {
            writer.write(output);
        }

        @Override
        public void close() throws IOException {
            writer.flush();
            writer.close();
            reader.close();
        }
    }
}