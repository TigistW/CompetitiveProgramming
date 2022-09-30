class Solution {
  public boolean validUtf8(int[] data) {
    int val = 0;

    for (final int d : data)
      if (val == 0) {
        if ((d >> 3) == 0b11110)
          val = 3;
        else if ((d >> 4) == 0b1110)
          val = 2;
        else if ((d >> 5) == 0b110)
          val = 1;
        else if ((d >> 7) == 0b0)
          val = 0;
        else
          return false;
      } else {
        if ((d >> 6) != 0b10)
          return false;
        --val;
      }

    return val == 0;
  }
}