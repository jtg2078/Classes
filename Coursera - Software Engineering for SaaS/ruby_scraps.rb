# metaprogramming to the rescue!

class Numeric
  @@currencies = {'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019}
  def method_missing(method_id)
    singular_currency = method_id.to_s.gsub( /s$/, '')
    if @@currencies.has_key?(singular_currency)
      self * @@currencies[singular_currency]
    else
      super
    end
  end
end

#print 12.rupee


x = [1,2,3]
x.send :[]=,0,2
#p x[0] + x.[](1) + x.send(:[],2)

class C
end

class B < C
end

class A < B
end

a = A.new
b = B.new
c = C.new

#p A.superclass == B
#p "\n"
#p a.superclass == b.class
#p a.class.ancestors.include?(C)
#p b.respond_to?('class')
#p b.class

class Book
	attr_accessor :author
	attr_reader :title
	attr_writer :comments
	def initialize(author, title)
		@author = author
		@title = title
		@comments = []
	end
end

book = Book.new("Chuck Palahniuk", "Fight Club")
p book.title
#book.comments.each { |comment| puts comment }
#book.comments << "#{book.title} was a good book"
#book.title = "Cooking Club"
book.comments = []
p "#{book.title} was written by #{book.author}." 