// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

import java.util.NoSuchElementException;

class PeekingIterator implements Iterator<Integer> {
    
    Integer tmp;
    Iterator<Integer> iter;
    boolean noSuchElement = false;
    
	public PeekingIterator(Iterator<Integer> iterator) {
	    this.iter = iterator;
        advanceIter();
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return tmp;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
        if (noSuchElement) {
            throw new NoSuchElementException();
        }
        Integer res = tmp;
        advanceIter();
        return res;
	}
	
	@Override
	public boolean hasNext() {
	    return !this.noSuchElement;
	}
    
    private void advanceIter() {
        if (iterator.hasNext()) {
            tmp = this.iter.next();
        } else {
            this.noSuchElement = true;
        }
    }
}