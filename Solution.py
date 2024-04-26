public int solution(int n) {
        // write your code in Java SE 8
        String binaryRep = Integer.toBinaryString(n);
        System.out.println("Binary Representation of " + n + " = " + binaryRep);
        List<String> strList = new ArrayList<String>();
        int count = 0;
        for (int i = 0; i < binaryRep.length(); i++) { // Loop through the each number 
            String str = binaryRep.charAt(i) + ""; // getting one by one number
            if(str.equals("0")){
                for(int j = i;j<binaryRep.length();j++){ //Get each next element
                    String str1 = binaryRep.charAt(j) + "";
                    if(!str.equals("1") &&  str.equals(str1)){
                        if(!strList.isEmpty() && count >= strList.size()){
                            strList.add(str1);
                        }else if(strList.isEmpty()){
                            strList.add(str1);
                        }
                        count ++; 
                    }else{
                        count = 0;
                        break;
                    }
                }
           }   
        }
        return strList.size();
    }