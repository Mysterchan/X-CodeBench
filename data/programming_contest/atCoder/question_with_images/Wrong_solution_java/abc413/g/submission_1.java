import java.util.*; import java.util.stream.*;
public class Main
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int H = Integer.valueOf(scan.next());
        int W = Integer.valueOf(scan.next());
        int K = Integer.valueOf(scan.next());
        Map<Long,Integer> square = new HashMap<>();
        Set<Long> topEnd = new HashSet<>();
        Set<Long> rightEnd = new HashSet<>();
        for (int k = 0;k < K;k++)
        {
            long r = Integer.valueOf(scan.next()) - 1;
            long c = Integer.valueOf(scan.next()) - 1;
            square.put(r * W + c,1);
            if (r == 0)
            {
                topEnd.add(c);
            }
            if (c == W - 1)
            {
                rightEnd.add(r);
            }
        }
        scan.close();
        int[][] d = {{-1,0},{1,0},{-1,-1},{0,-1},{1,-1},{-1,1},{0,1},{1,1}};
        for (long topW : topEnd)
        {
            ArrayDeque<Place> next = new ArrayDeque<>();
            next.add(new Place(0,topW));
            while (!next.isEmpty())
            {
                Place p = next.pollFirst();
                for (int k = 0;k < d.length;k++)
                {
                    long nextH = p.h + d[k][0];
                    long nextW = p.w + d[k][1];
                    if (0 <= nextH && nextH < H && 0 <= nextW && nextW < W)
                    {
                        long index = nextH * W + nextW;
                        if (square.containsKey(index))
                        {
                            if (square.get(index) == 1)
                            {
                                square.put(index,2);
                                next.add(new Place(nextH, nextW));
                                if (nextH == H - 1 || nextW == 0)
                                {
                                    System.out.println("No");
                                    return;
                                }
                            }

                        }
                    }
                }
            }
        }

        for (long rightH : rightEnd)
        {
            ArrayDeque<Place> next = new ArrayDeque<>();
            next.add(new Place(rightH,W - 1));
            while (!next.isEmpty())
            {
                Place p = next.pollFirst();
                for (int k = 0;k < d.length;k++)
                {
                    long nextH = p.h + d[k][0];
                    long nextW = p.w + d[k][1];
                    if (0 <= nextH && nextH < H && 0 <= nextW && nextW < W)
                    {
                        long index = nextH * W + nextW;
                        if (square.containsKey(index))
                        {
                            if (square.get(index) == 1 || square.get(index) == 2)
                            {
                                square.put(index,3);
                                next.add(new Place(nextH, nextW));

                                if (nextH == H - 1 || nextW == 0)
                                {
                                    System.out.println("No");
                                    return;
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.println("Yes");
    }
    public static void wait(int sec)
    {
        try {

            Thread.sleep(sec * 1000);
        } catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
class Place
{
    long h;
    long w;
    Place(long h, long w)
    {
        this.h = h;
        this.w = w;
    }
}