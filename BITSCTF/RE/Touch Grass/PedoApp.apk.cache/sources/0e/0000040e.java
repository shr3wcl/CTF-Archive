package z0;

import f0.q;

/* loaded from: classes.dex */
public abstract class a<T> implements b<T> {

    /* JADX INFO: Access modifiers changed from: package-private */
    @kotlin.coroutines.jvm.internal.f(c = "kotlinx.coroutines.flow.AbstractFlow", f = "Flow.kt", l = {212}, m = "collect")
    /* renamed from: z0.a$a  reason: collision with other inner class name */
    /* loaded from: classes.dex */
    public static final class C0042a extends kotlin.coroutines.jvm.internal.d {

        /* renamed from: d  reason: collision with root package name */
        Object f1623d;

        /* renamed from: e  reason: collision with root package name */
        /* synthetic */ Object f1624e;

        /* renamed from: f  reason: collision with root package name */
        final /* synthetic */ a<T> f1625f;

        /* renamed from: g  reason: collision with root package name */
        int f1626g;

        /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
        C0042a(a<T> aVar, i0.d<? super C0042a> dVar) {
            super(dVar);
            this.f1625f = aVar;
        }

        @Override // kotlin.coroutines.jvm.internal.a
        public final Object invokeSuspend(Object obj) {
            this.f1624e = obj;
            this.f1626g |= Integer.MIN_VALUE;
            return this.f1625f.a(null, this);
        }
    }

    /* JADX WARN: Removed duplicated region for block: B:10:0x0023  */
    /* JADX WARN: Removed duplicated region for block: B:18:0x0037  */
    @Override // z0.b
    /*
        Code decompiled incorrectly, please refer to instructions dump.
        To view partially-correct code enable 'Show inconsistent code' option in preferences
    */
    public final java.lang.Object a(z0.c<? super T> r6, i0.d<? super f0.q> r7) {
        /*
            r5 = this;
            boolean r0 = r7 instanceof z0.a.C0042a
            if (r0 == 0) goto L13
            r0 = r7
            z0.a$a r0 = (z0.a.C0042a) r0
            int r1 = r0.f1626g
            r2 = -2147483648(0xffffffff80000000, float:-0.0)
            r3 = r1 & r2
            if (r3 == 0) goto L13
            int r1 = r1 - r2
            r0.f1626g = r1
            goto L18
        L13:
            z0.a$a r0 = new z0.a$a
            r0.<init>(r5, r7)
        L18:
            java.lang.Object r7 = r0.f1624e
            java.lang.Object r1 = j0.b.c()
            int r2 = r0.f1626g
            r3 = 1
            if (r2 == 0) goto L37
            if (r2 != r3) goto L2f
            java.lang.Object r6 = r0.f1623d
            a1.c r6 = (a1.c) r6
            f0.l.b(r7)     // Catch: java.lang.Throwable -> L2d
            goto L4f
        L2d:
            r7 = move-exception
            goto L59
        L2f:
            java.lang.IllegalStateException r6 = new java.lang.IllegalStateException
            java.lang.String r7 = "call to 'resume' before 'invoke' with coroutine"
            r6.<init>(r7)
            throw r6
        L37:
            f0.l.b(r7)
            a1.c r7 = new a1.c
            i0.g r2 = r0.getContext()
            r7.<init>(r6, r2)
            r0.f1623d = r7     // Catch: java.lang.Throwable -> L55
            r0.f1626g = r3     // Catch: java.lang.Throwable -> L55
            java.lang.Object r6 = r5.b(r7, r0)     // Catch: java.lang.Throwable -> L55
            if (r6 != r1) goto L4e
            return r1
        L4e:
            r6 = r7
        L4f:
            r6.releaseIntercepted()
            f0.q r6 = f0.q.f235a
            return r6
        L55:
            r6 = move-exception
            r4 = r7
            r7 = r6
            r6 = r4
        L59:
            r6.releaseIntercepted()
            throw r7
        */
        throw new UnsupportedOperationException("Method not decompiled: z0.a.a(z0.c, i0.d):java.lang.Object");
    }

    public abstract Object b(c<? super T> cVar, i0.d<? super q> dVar);
}