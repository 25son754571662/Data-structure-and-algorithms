## 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

思路：用一个栈（A）的入栈代替入队操作，另一个栈（B）的出栈代替出队操作

特殊情况：如果当前需要出栈，但此时栈B为空时，可以将栈A的元素出栈，并入栈到B中，然后再进行出栈操作

想象一下将两个栈，栈底互相贴住，它们就可以形成一个队列了。而上面的特殊情况就只不过是，将元素往右挪动了一下而已
