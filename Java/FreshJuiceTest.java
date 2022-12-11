class FreshJuice {
    enum FreshJuiceSize( MEDIUM )

    FreshJuiceSize size;
}

public class FreshJuiceTest {
    public static void main(String args[]){
        FreshJuice juice = new FreshJuice();
        juice.size = FreshJuice. FreshJuiceSize.MEDIUM ;
    }
}