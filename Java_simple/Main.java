import java.io.*;

public class Main {

    public static void main(String[] args) {

        try {

            ProcessBuilder pb =
                    new ProcessBuilder(
                            "python",
                            "hello.py"
                    );

            Process process = pb.start();

            BufferedReader output =
                    new BufferedReader(
                            new InputStreamReader(
                                    process.getInputStream()
                            )
                    );

            BufferedReader error =
                    new BufferedReader(
                            new InputStreamReader(
                                    process.getErrorStream()
                            )
                    );

            String line;

            System.out.println("OUTPUT:");

            while ((line = output.readLine()) != null) {
                System.out.println(line);
            }

            System.out.println("ERROR:");

            while ((line = error.readLine()) != null) {
                System.out.println(line);
            }

        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}