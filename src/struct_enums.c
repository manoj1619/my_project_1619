// ❌ BAD: typedef name not following s_MyStruct or e_MyEnum convention
//typedef struct {
//  int value;
//} mystruct_t;

//typedef enum { RED, GREEN, BLUE } myenum_t;

// ✅ GOOD:
typedef struct {
  int value;
} s_MyStruct;

typedef enum { RED, GREEN, BLUE } e_MyEnum;
