import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.Collator;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

// java -cp "$env:USERPROFILE\.m2\repository\com\googlecode\ez-vcard\ez-vcard\0.12.0\ez-vcard-0.12.0.jar" .\VCFParser.java

/**
 * <dependency>
 *     <groupId>com.googlecode.ez-vcard</groupId>
 *     <artifactId>ez-vcard</artifactId>
 *     <version>0.12.0</version>
 * </dependency>
 */
import ezvcard.Ezvcard;
import ezvcard.VCard;
import ezvcard.property.FormattedName;

public class VCFParser {

    // 排序a-z
    public static void sort(List<VCard> vCards) {
        System.out.println(vCards.size() + "个联系人待排序");
        Collator collator = Collator.getInstance(Locale.CHINESE);

        vCards.sort((a, b) -> {
            FormattedName fn1 = a.getFormattedName();
            FormattedName fn2 = b.getFormattedName();
            if (fn1 == null || fn2 == null) {
                return 0;
            }
            return collator.compare(fn1.getValue(), fn2.getValue());
        });
        System.out.println("排序完成");
    }

    // 扫描指定路径下的vcf文件
    public static List<Path> scan(Path path) throws IOException {
        System.out.println("正在扫描" + path.toString() + "下的文件...");
        List<Path> vcfFiles = Files.list(path)
                .filter(p -> p.toString().toLowerCase().endsWith(".vcf"))
                .collect(Collectors.toList());
        System.out.println("扫描完成，共扫描到" + vcfFiles.size() + "个文件");
        return vcfFiles;
    }

    // 读取vcf
    public static List<VCard> read(String pathStr) throws IOException {
        System.out.println("读取" + pathStr + "...");
        Path path = Paths.get(pathStr);
        List<VCard> mergeList = null;
        if (path.toFile().isFile()) {
            // 文件
            mergeList = Ezvcard.parse(path).all();
        } else if (path.toFile().isDirectory()) {
            // 目录
            List<Path> vcfFiles = scan(path);
            if (vcfFiles.size() > 0) {
                mergeList = new ArrayList<>();
            }
            for (Path vcfFile : vcfFiles) {
                System.out.println("读取" + vcfFile + "...");
                List<VCard> vCard = Ezvcard.parse(vcfFile).all();
                VCard card = vCard.get(0);
                mergeList.add(card);
            }
        }
        if (mergeList == null) {
            System.out.println("读取失败");
            System.exit(1);
        }

        System.out.println("读取完成");
        System.out.println("共读取" + mergeList.size() + "个联系人");
        return mergeList;
    }

    // 创建一个输出流
    public static OutputStreamWriter getOneOutputStreamWriter(String pathStr, boolean append) throws IOException {
        if (pathStr == null) {
            pathStr = "./" + System.currentTimeMillis() + ".vcf";
            System.out.println("创建文件" + pathStr);
        }
        Path path = Paths.get(pathStr);
        if (!path.toFile().exists()) {
            Files.createDirectories(path.getParent());
            path.toFile().createNewFile();
        }
        FileOutputStream fileOutputStream = new FileOutputStream(path.toFile(), append);
        return new OutputStreamWriter(fileOutputStream, "utf-8");
    }

    // 按照FN写出到不同的文件
    public static void map(List<VCard> vCards) throws IOException {
        System.out.println("mapping...");
        for (VCard vCard : vCards) {
            String fn = vCard.getFormattedName().getValue();
            try (OutputStreamWriter osw = getOneOutputStreamWriter("./tmp/" + fn + ".vcf", true)) {
                Ezvcard.write(vCard).prodId(false).go(osw);
            }
        }
        System.out.println("mapped");
    }

    // 合并不冲突的文件
    public static List<VCard> merge() throws IOException {
        List<Path> vcfFiles = scan(Paths.get("./tmp"));
        // 合并所有的vcf文件
        List<VCard> mergeList = new ArrayList<>();
        for (Path vcfFile : vcfFiles) {
            List<VCard> vCard = Ezvcard.parse(vcfFile).all();
            if (vCard.size() != 1) {
                // 如果vcf文件包含不止一个vcard，跳过
                continue;
            }
            System.out.println("正在合并" + vcfFile);
            VCard card = vCard.get(0);
            mergeList.add(card);
            // 删除文件
            vcfFile.toFile().delete();
        }
        System.out.println("合并完成，共合并" + mergeList.size() + "个联系人");
        return mergeList;
    }

    // 写出vcf
    public static void write(List<VCard> vCards) throws IOException {
        System.out.println("写出" + vCards.size() + "个联系人");
        try (OutputStreamWriter osw = getOneOutputStreamWriter(null, false)) {
            Ezvcard.write(vCards).prodId(false).go(osw);
            System.out.println("写出完成");
        }
    }

    // 处理冲突
    public static void handleConflict() throws IOException {
        List<Path> paths = scan(Paths.get("./tmp"));
        if (paths.size() < 1) {
            System.out.println("恭喜，没有冲突需要处理");
            return;
        }
        for (int i = 0; i < paths.size(); i++) {
            Path path = paths.get(i);
            System.out.print((i + 1) + "/" + paths.size() + " " + path);
            Runtime.getRuntime().exec("cmd /c code " + path.toString());
            // 按任意键继续
            System.in.read();
            System.in.read();// 回车会被当成两个字符
        }

        List<VCard> vCards = read("./tmp");
        sort(vCards);
        write(vCards);
    }

    // 处理vcf文件
    public static void process(String pathStr) throws IOException {
        List<VCard> vCards = read(pathStr);
        map(vCards);
        List<VCard> mergedCards = merge();
        sort(mergedCards);
        write(mergedCards);
        handleConflict();
    }

    public static void main(String[] args) throws IOException {
        process("./1691723970765.vcf");
    }

}